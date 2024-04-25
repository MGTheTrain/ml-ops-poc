module "main" {
  source = "git::https://github.com/MGTheTrain/gitops-ftw.git//terraform/modules/az?ref=main"
  digital_product_affix       = var.digital_product_affix
  environment                 = var.environment
  resource_instance_number    = var.resource_instance_number
  location                    = var.location
  team                        = var.team
  number_of_storage_accounts  = var.number_of_storage_accounts
  sa_account_tier             = var.sa_account_tier
  sa_account_replication_type = var.sa_account_replication_type
  sc_container_access_type    = var.sc_container_access_type
}