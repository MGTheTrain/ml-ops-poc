# External helm charts

resource "kubernetes_namespace" "external_services" {
  metadata {
    annotations = local.tags
    labels      = local.tags
    name        = "external-services"
  }
}

# The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup

# mlflow helm chart
resource "helm_release" "mlflow" {
  name       = "mlflow"
  repository = "https://community-charts.github.io/helm-charts"
  chart      = "mlflow"
  version    = "0.7.19"
  namespace  = kubernetes_namespace.external_services.metadata.0.name
  count      = var.ml_ops_tool == "mlflow" ? 1 : 0
}

# Nginx controller and Ingress
resource "helm_release" "nginx_ingress_controller" {
  name       = "nginx-ingress-controller"
  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"
  version    = "4.10.0"
  namespace  = kubernetes_namespace.external_services.metadata.0.name

  set {
    name  = "service.type"
    value = "LoadBalancer"
  }
}