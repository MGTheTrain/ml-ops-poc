resource "kubernetes_namespace" "ml_ops_ftw_namespace" {
  metadata {
    annotations = local.tags
    labels      = local.tags
    name        = "ml-ops-ftw"
  }
}

resource "kubernetes_secret" "acr_secret" {
  metadata {
    name        = "acr-secret"
    namespace   = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name
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

# The installation of Kubeflow will be managed externally through the continuous delivery (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup

# mlflow helm chart
resource "helm_release" "mlflow" {
  name       = "mlflow"
  repository = "https://community-charts.github.io/helm-charts"
  chart      = "mlflow"
  version    = "0.7.19"
  namespace  = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name
  count      = var.ml_ops_tool == "mlflow" ? 1 : 0
}

# Nginx controller and Ingress
resource "helm_release" "nginx_ingress_controller" {
  name       = "nginx-ingress-controller"
  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"
  version    = "4.10.0"
  namespace  = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name

  set {
    name  = "service.type"
    value = "LoadBalancer"
  }
}

resource "kubernetes_ingress_v1" "ml_ops_ftw_ingress" {
  wait_for_load_balancer = true
  metadata {
    name        = "ml-ops-ftw-ingress"
    namespace   = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name
    annotations = local.tags
    labels      = local.tags
  }
  spec {
    ingress_class_name = "nginx"
    rule {
      http {
        # path {
        #   backend {
        #     service {
        #       name = "hello-world-service"
        #       port {
        #         number = 80
        #       }
        #     }
        #   }
        #   path = "/api/v1/hws"
        # }
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