# ACR
output "container_registry_admin_username_list" {
  value = module.acr.container_registry_admin_username_list
}

output "container_registry_admin_password_list" {
  value     = module.acr.container_registry_admin_password_list
  sensitive = true
}

output "container_registry_login_server_list" {
  value = module.acr.container_registry_login_server_list
}