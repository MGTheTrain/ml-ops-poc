output "resource_group_name" {
  value = module.az.resource_group_name
}

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