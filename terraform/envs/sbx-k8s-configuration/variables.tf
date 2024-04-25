variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string
}

# K8s
variable "acr_login_server_name" {
  default     = "TBD"
  sensitive   = true
  description = "Sets an ACR registry server name."
}

variable "acr_username" {
  default     = "TBD"
  sensitive   = true
  description = "Sets an ACR user name."
}

variable "acr_password" {
  default     = "TBD"
  sensitive   = true
  description = "Sets an ACR password."
}

variable "ml_ops_tool" {
  description = "String determining whether to install mlflow or none. Viable options: [ mlflow, kubeflow, none ]. The installation of Kubeflow will be managed externally through the continuous delivery (CD) workflow, as Terraform modules and kubernetes provider are either outdated or difficult to setup"
  type        = string
  default     = "none"
}