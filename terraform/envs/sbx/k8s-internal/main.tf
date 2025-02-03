module "k8s_internal" {
  source                  = "../../../modules/k8s-internal"
  environment             = var.environment
  acr_login_server_name   = var.acr_login_server_name
  acr_username            = var.acr_username
  acr_password            = var.acr_password
  az_sa_connection_string = var.az_sa_connection_string
  az_sa_container_name    = var.az_sa_container_name
}