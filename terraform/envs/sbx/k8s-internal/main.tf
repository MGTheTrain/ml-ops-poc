module "k8s_internal" {
  source                = "../../../modules/k8s-internal"
  environment           = var.environment
  acr_login_server_name = var.acr_login_server_name
  acr_username          = var.acr_username
  acr_password          = var.acr_password
}