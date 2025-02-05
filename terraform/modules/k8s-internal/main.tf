resource "kubernetes_namespace" "internal_apps" {
  metadata {
    annotations = local.tags
    labels      = local.tags
    name        = "internal-apps"
  }
}

resource "kubernetes_secret" "acr_secret" {
  metadata {
    name        = "acr-secret"
    namespace   = kubernetes_namespace.internal_apps.metadata.0.name
    annotations = local.tags
    labels      = local.tags
  }
  type = "kubernetes.io/dockerconfigjson"
  data = {
    ".dockerconfigjson" = jsonencode({
      auths = {
        "${var.acr_login_server_name}" = {
          "username" = var.acr_username
          "password" = var.acr_password
          "auth"     = base64encode("${var.acr_username}:${var.acr_password}")
        }
      }
    })
  }
}

resource "kubernetes_secret" "storage_account_secret" {
  metadata {
    name        = "storage-account-secret"
    namespace   = kubernetes_namespace.internal_apps.metadata.0.name
    annotations = local.tags
    labels      = local.tags
  }

  type = "Opaque"

  data = {
    "connection_string" = var.az_sa_connection_string
    "container_name"    = var.az_sa_container_name
  }
}

resource "kubernetes_ingress_v1" "nginx_controller_ingress" {
  wait_for_load_balancer = true
  metadata {
    name        = "ml-ops-poc-ingress"
    namespace   = kubernetes_namespace.internal_apps.metadata.0.name
    annotations = local.tags
    labels      = local.tags
  }
  spec {
    ingress_class_name = "nginx"
    rule {
      http {
        path {
          backend {
            service {
              name = "inference-service"
              port {
                number = 80
              }
            }
          }
          path = "/api/v1/hws"
        }
        path {
          backend {
            service {
              name = "nginx-app"
              port {
                number = 80
              }
            }
          }
          path = "/"
        }
      }
    }
  }
}