<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_az"></a> [az](#module\_az) | git::https://github.com/MGTheTrain/gitops-ftw.git//terraform/modules/az | main |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aks_admin_username"></a> [aks\_admin\_username](#input\_aks\_admin\_username) | The AKS admin username | `string` | `"azureuser"` | no |
| <a name="input_aks_enable_auto_scaling"></a> [aks\_enable\_auto\_scaling](#input\_aks\_enable\_auto\_scaling) | Whether to allow the AKS cluster to automatically adjust the number of nodes in a node pool | `bool` | `true` | no |
| <a name="input_aks_max_node_count"></a> [aks\_max\_node\_count](#input\_aks\_max\_node\_count) | The AKS max node count | `number` | `2` | no |
| <a name="input_aks_node_count"></a> [aks\_node\_count](#input\_aks\_node\_count) | The AKS node count | `number` | `1` | no |
| <a name="input_aks_os_disk_size_gb"></a> [aks\_os\_disk\_size\_gb](#input\_aks\_os\_disk\_size\_gb) | The AKS Agent Operating System disk size in GB | `string` | `"128"` | no |
| <a name="input_aks_vm_size"></a> [aks\_vm\_size](#input\_aks\_vm\_size) | The AKS vm size. Other option is Standard\_B2s. See https://learn.microsoft.com/en-us/azure/virtual-machines/sizes, https://azureprice.net/ | `string` | `"Standard_B8ms"` | no |
| <a name="input_digital_product_affix"></a> [digital\_product\_affix](#input\_digital\_product\_affix) | The digital product affix. | `string` | `"mlopsftw"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_location"></a> [location](#input\_location) | The geographic location in which to deploy. | `string` | `"West Europe"` | no |
| <a name="input_number_of_aks"></a> [number\_of\_aks](#input\_number\_of\_aks) | The total number of AKses to deploy. | `number` | `1` | no |
| <a name="input_resource_instance_number"></a> [resource\_instance\_number](#input\_resource\_instance\_number) | The resource instance number. | `string` | `"001"` | no |
| <a name="input_team"></a> [team](#input\_team) | The team used for tagging resource groups and resources. | `string` | `"MG Innovators"` | no |
| <a name="input_virtual_network_address_space"></a> [virtual\_network\_address\_space](#input\_virtual\_network\_address\_space) | The virtual network address space. E.g. 2^(32-16)=65536 private ips in Vnet. | `list(string)` | <pre>[<br>  "10.1.0.0/16"<br>]</pre> | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_aks_kube_config_list"></a> [aks\_kube\_config\_list](#output\_aks\_kube\_config\_list) | n/a |
| <a name="output_aks_name_list"></a> [aks\_name\_list](#output\_aks\_name\_list) | n/a |
| <a name="output_aks_tls_private_key"></a> [aks\_tls\_private\_key](#output\_aks\_tls\_private\_key) | n/a |
| <a name="output_resource_group_name"></a> [resource\_group\_name](#output\_resource\_group\_name) | n/a |
<!-- END_TF_DOCS -->