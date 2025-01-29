<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | >= 2.5.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [helm_release.mlflow](https://registry.terraform.io/providers/helm/latest/docs/resources/release) | resource |
| [helm_release.nginx_ingress_controller](https://registry.terraform.io/providers/helm/latest/docs/resources/release) | resource |
| [kubernetes_ingress_v1.ml_ops_ftw_ingress](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/ingress_v1) | resource |
| [kubernetes_namespace.ml_ops_ftw_namespace](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/namespace) | resource |
| [kubernetes_secret.acr_secret](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/secret) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_acr_login_server_name"></a> [acr\_login\_server\_name](#input\_acr\_login\_server\_name) | Sets an ACR registry server name. | `string` | `"TBD"` | no |
| <a name="input_acr_password"></a> [acr\_password](#input\_acr\_password) | Sets an ACR password. | `string` | `"TBD"` | no |
| <a name="input_acr_username"></a> [acr\_username](#input\_acr\_username) | Sets an ACR user name. | `string` | `"TBD"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_ml_ops_tool"></a> [ml\_ops\_tool](#input\_ml\_ops\_tool) | String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup | `string` | `"none"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ml_ops_ftw_namespace"></a> [ml\_ops\_ftw\_namespace](#output\_ml\_ops\_ftw\_namespace) | n/a |
<!-- END_TF_DOCS -->