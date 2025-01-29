<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | =3.0.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_acr"></a> [acr](#module\_acr) | git::https://github.com/MGTheTrain/gitops-poc.git//devops/terraform/acr | main |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_acr_admin_enabled"></a> [acr\_admin\_enabled](#input\_acr\_admin\_enabled) | Flag to enable admin user for the Azure Container Registry | `bool` | `true` | no |
| <a name="input_acr_sku"></a> [acr\_sku](#input\_acr\_sku) | SKU for the Azure Container Registry | `string` | `"Basic"` | no |
| <a name="input_digital_product_affix"></a> [digital\_product\_affix](#input\_digital\_product\_affix) | The digital product affix of the acr module. | `string` | `"mopocacr"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_location"></a> [location](#input\_location) | The geographic location in which to deploy. | `string` | `"Switzerland North"` | no |
| <a name="input_number_of_container_registries"></a> [number\_of\_container\_registries](#input\_number\_of\_container\_registries) | The total number of Azure Container registries to deploy. | `number` | `1` | no |
| <a name="input_resource_instance_number"></a> [resource\_instance\_number](#input\_resource\_instance\_number) | The resource instance number. | `string` | `"001"` | no |
| <a name="input_team"></a> [team](#input\_team) | The team used for tagging resource groups and resources. | `string` | `"MG Innovators"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_container_registry_admin_password_list"></a> [container\_registry\_admin\_password\_list](#output\_container\_registry\_admin\_password\_list) | n/a |
| <a name="output_container_registry_admin_username_list"></a> [container\_registry\_admin\_username\_list](#output\_container\_registry\_admin\_username\_list) | ACR |
| <a name="output_container_registry_login_server_list"></a> [container\_registry\_login\_server\_list](#output\_container\_registry\_login\_server\_list) | n/a |
<!-- END_TF_DOCS -->