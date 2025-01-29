variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string

  validation {
    condition     = can(regex("^(sbx|dev|qas|prd)$", var.environment))
    error_message = "Invalid input, options: \"sbx\", \"dev\", \"qas\", \"prd\"."
  }
}

variable "ml_ops_tool" {
  description = "String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous deployment (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup"
  type        = string
  default     = "none"

  validation {
    condition     = var.ml_ops_tool == "none" || var.ml_ops_tool == "kubeflow" || var.ml_ops_tool == "mlflow"
    error_message = "ml_ops_tool must be either 'none', 'kubeflow' or 'mlflow'"
  }
}
