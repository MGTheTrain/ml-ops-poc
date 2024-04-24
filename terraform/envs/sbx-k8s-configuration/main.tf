module "k8s" {
  source                = "../../modules/k8s"
  environment           = var.environment
  acr_login_server_name = var.acr_login_server_name
  acr_username          = var.acr_username
  acr_password          = var.acr_password
  ml_ops_tool           = var.ml_ops_tool
}