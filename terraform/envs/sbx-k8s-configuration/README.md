<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | >= 2.5.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_k8s"></a> [k8s](#module\_k8s) | ../../modules/k8s | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_acr_login_server_name"></a> [acr\_login\_server\_name](#input\_acr\_login\_server\_name) | Sets an ACR registry server name. | `string` | `"TBD"` | no |
| <a name="input_acr_password"></a> [acr\_password](#input\_acr\_password) | Sets an ACR password. | `string` | `"TBD"` | no |
| <a name="input_acr_username"></a> [acr\_username](#input\_acr\_username) | Sets an ACR user name. | `string` | `"TBD"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_ml_ops_tool"></a> [ml\_ops\_tool](#input\_ml\_ops\_tool) | String determining whether to install Argo CD or FluxCD. Viable options: [ kubeflow, fluxcd ] | `string` | `"kubeflow"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ml_ops_ftw_namespace"></a> [ml\_ops\_ftw\_namespace](#output\_ml\_ops\_ftw\_namespace) | n/a |
<!-- END_TF_DOCS -->