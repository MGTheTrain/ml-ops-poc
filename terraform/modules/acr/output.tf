# Azure Container registry
output "container_registry_admin_username_list" {
  value = [for container_registry in azurerm_container_registry.this : container_registry.admin_username]
}

output "container_registry_admin_password_list" {
  value = [for container_registry in azurerm_container_registry.this : container_registry.admin_password]
  sensitive = true
}

output "container_registry_login_server_list" {
  value = [for container_registry in azurerm_container_registry.this : container_registry.login_server]
}