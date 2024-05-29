module "main" {
  source                      = "git::https://github.com/MGTheTrain/gitops-poc.git//devops/terraform?ref=main"
  digital_product_affix       = var.digital_product_affix_sa
  environment                 = var.environment
  resource_instance_number    = var.resource_instance_number
  location                    = var.location
  team                        = var.team
  number_of_storage_accounts  = var.number_of_storage_accounts
  sa_account_tier             = var.sa_account_tier
  sa_account_replication_type = var.sa_account_replication_type
  sc_container_access_type    = var.sc_container_access_type
}

module "acr" {
  source                         = "../../terraform/modules/acr"
  digital_product_affix          = var.digital_product_affix_acr_module
  environment                    = var.environment
  resource_instance_number       = var.resource_instance_number
  location                       = var.location
  team                           = var.team
  number_of_container_registries = var.number_of_container_registries
  acr_sku                        = var.acr_sku
  acr_admin_enabled              = var.acr_admin_enabled
}