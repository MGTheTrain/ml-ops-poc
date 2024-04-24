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


# Install Operator Lifecycle Manager (OLM). Required for the Kubeflow operator
resource "null_resource" "install_olm" {
  provisioner "local-exec" {
    command = "curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.27.0/install.sh | bash -s v0.27.0"
  }
  count = var.ml_ops_tool == "kubeflow" ? 1 : 0
}

# Install the Kubeflow operator
resource "kubernetes_manifest" "install_kubeflow_operator" {
  manifest = {
    metadata = {
      name      = "kubeflow-operator"
      namespace = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name
    }

    spec = {
      api_version = "operators.coreos.com/v1alpha1"
      kind        = "Subscription"

      spec = {
        name             = "kubeflow"
        channel          = "alpha"
        source           = "operatorhubio-catalog"
        source_namespace = "olm"
      }
    }
  }
  count = var.ml_ops_tool == "kubeflow" ? 1 : 0
}

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