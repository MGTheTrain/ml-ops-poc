<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [helm_release.mlflow](https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release) | resource |
| [helm_release.nginx_ingress_controller](https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release) | resource |
| [kubernetes_namespace.external_services](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/namespace) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_ml_ops_tool"></a> [ml\_ops\_tool](#input\_ml\_ops\_tool) | String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup | `string` | `"none"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_external_services_namespace"></a> [external\_services\_namespace](#output\_external\_services\_namespace) | n/a |
<!-- END_TF_DOCS -->