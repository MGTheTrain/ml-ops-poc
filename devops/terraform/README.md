<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | =3.0.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_main"></a> [main](#module\_main) | https://github.com/MGTheTrain/gitops-ftw.git//devops/terraform | main |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_digital_product_affix"></a> [digital\_product\_affix](#input\_digital\_product\_affix) | The digital product affix. | `string` | `"gftfbe"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_location"></a> [location](#input\_location) | The geographic location in which to deploy. | `string` | `"West Europe"` | no |
| <a name="input_number_of_storage_accounts"></a> [number\_of\_storage\_accounts](#input\_number\_of\_storage\_accounts) | The total number of Azure Storage Accounts to deploy. | `number` | `1` | no |
| <a name="input_resource_instance_number"></a> [resource\_instance\_number](#input\_resource\_instance\_number) | The resource instance number. | `string` | `"001"` | no |
| <a name="input_sa_account_replication_type"></a> [sa\_account\_replication\_type](#input\_sa\_account\_replication\_type) | Account replication type for the Azure Storage Account | `string` | `"LRS"` | no |
| <a name="input_sa_account_tier"></a> [sa\_account\_tier](#input\_sa\_account\_tier) | Account tier for the Azure Storage Account | `string` | `"Standard"` | no |
| <a name="input_sc_container_access_type"></a> [sc\_container\_access\_type](#input\_sc\_container\_access\_type) | Container access type of the Storage Account Container | `string` | `"private"` | no |
| <a name="input_team"></a> [team](#input\_team) | The team used for tagging resource groups and resources. | `string` | `"MG Innovators"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->