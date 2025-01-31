<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | >= 2.5.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_k8s_external_helm"></a> [k8s\_external\_helm](#module\_k8s\_external\_helm) | ../../../modules/k8s-external-helm | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | The environment. | `string` | `"sbx"` | no |
| <a name="input_ml_ops_tool"></a> [ml\_ops\_tool](#input\_ml\_ops\_tool) | String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup | `string` | `"none"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->