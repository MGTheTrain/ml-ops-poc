variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string
}

variable "ml_ops_tool" {
  description = "String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup"
  type        = string
  default     = "none"
}