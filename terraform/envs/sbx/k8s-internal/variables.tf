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

variable "az_sa_connection_string" {
  default     = "TBD"
  sensitive   = true
  type        = string
  description = "The Azure Storage Account connection string"
}

variable "az_sa_container_name" {
  default     = "TBD"
  sensitive   = true
  type        = string
  description = "The Azure Storage Account container name"
}