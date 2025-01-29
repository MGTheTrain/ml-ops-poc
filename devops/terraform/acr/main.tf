module "acr" {
  source                         = "git::https://github.com/MGTheTrain/gitops-poc.git//devops/terraform/acr?ref=main"
  digital_product_affix          = var.digital_product_affix
  environment                    = var.environment
  resource_instance_number       = var.resource_instance_number
  location                       = var.location
  team                           = var.team
  number_of_container_registries = var.number_of_container_registries
  acr_sku                        = var.acr_sku
  acr_admin_enabled              = var.acr_admin_enabled
}