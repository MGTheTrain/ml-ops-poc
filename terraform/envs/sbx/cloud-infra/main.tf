module "az" {
  source                        = "git::https://github.com/MGTheTrain/gitops-poc.git//terraform/modules/az?ref=main"
  digital_product_affix         = var.digital_product_affix
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