output "resource_group_name" {
  value = module.main.resource_group_name
}

output "aks_tls_private_key" {
  value     = module.main.aks_tls_private_key
  sensitive = true
}

output "aks_name_list" {
  value = module.main.aks_name_list
}

output "aks_kube_config_list" {
  value     = module.main.aks_kube_config_list
  sensitive = true
}