output "resource_group_name" {
  value = module.az.resource_group_name
}

# AKS
output "aks_tls_private_key" {
  value     = module.az.aks_tls_private_key
  sensitive = true
}

output "aks_name_list" {
  value = module.az.aks_name_list
}

output "aks_kube_config_list" {
  value     = module.az.aks_kube_config_list
  sensitive = true
}

# ACR
output "container_registry_admin_username_list" {
  value = module.acr.container_registry_admin_username_list
}

output "container_registry_admin_password_list" {
  value = module.acr.container_registry_admin_password_list
  sensitive = true
}

output "container_registry_login_server_list" {
  value = module.acr.container_registry_login_server_list
}