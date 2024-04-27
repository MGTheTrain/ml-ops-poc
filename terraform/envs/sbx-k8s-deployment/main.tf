module "az" {
  source                        = "git::https://github.com/MGTheTrain/gitops-ftw.git//terraform/modules/az?ref=main"
  digital_product_affix         = var.digital_product_affix_az_module
  environment                   = var.environment
  resource_instance_number      = var.resource_instance_number
  location                      = var.location
  team                          = var.team
  virtual_network_address_space = var.virtual_network_address_space
  number_of_aks                 = var.number_of_aks
  aks_admin_username            = var.aks_admin_username
  aks_enable_auto_scaling       = var.aks_enable_auto_scaling
  aks_node_count                = var.aks_node_count
  aks_max_node_count            = var.aks_max_node_count
  aks_vm_size                   = var.aks_vm_size
  aks_os_disk_size_gb           = var.aks_os_disk_size_gb
}

module "acr" {
  source                = "../../modules/acr"
  digital_product_affix = var.digital_product_affix_acr_module
  environment = var.environment
  resource_instance_number = var.resource_instance_number
  location = var.location
  team = var.team
  number_of_container_registries = var.number_of_container_registries
  acr_sku = var.acr_sku
  acr_admin_enabled = var.acr_admin_enabled
}