module "k8s_external_helm" {
  source      = "../../../modules/k8s-external-helm"
  environment = var.environment
  ml_ops_tool = var.ml_ops_tool
}