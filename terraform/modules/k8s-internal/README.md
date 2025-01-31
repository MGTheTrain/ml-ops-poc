<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [kubernetes_ingress_v1.nginx_controller_ingress](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/ingress_v1) | resource |
| [kubernetes_namespace.internal_apps](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/namespace) | resource |
| [kubernetes_secret.acr_secret](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/secret) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_acr_login_server_name"></a> [acr\_login\_server\_name](#input\_acr\_login\_server\_name) | Sets an ACR registry server name. | `string` | `"TBD"` | no |
| <a name="input_acr_password"></a> [acr\_password](#input\_acr\_password) | Sets an ACR password. | `string` | `"TBD"` | no |
| <a name="input_acr_username"></a> [acr\_username](#input\_acr\_username) | Sets an ACR user name. | `string` | `"TBD"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_internal_apps_namespace"></a> [internal\_apps\_namespace](#output\_internal\_apps\_namespace) | n/a |
<!-- END_TF_DOCS -->