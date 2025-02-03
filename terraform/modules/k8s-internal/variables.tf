variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string

  validation {
    condition     = can(regex("^(sbx|dev|qas|prd)$", var.environment))
    error_message = "Invalid input, options: \"sbx\", \"dev\", \"qas\", \"prd\"."
  }
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
  type        = string
  description = "The Azure Storage Account connection string"
}

variable "az_sa_container_name" {
  default     = "TBD"
  type        = string
  description = "The Azure Storage Account container name"
}

variable "az_sa_blob_name" {
  default     = "TBD"
  type        = string
  description = "The Azure Storage Account container blob name"
}
