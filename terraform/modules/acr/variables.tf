# Azure Rg
variable "digital_product_affix" {
  default     = "mlopftwsacr"
  description = "The digital product affix."
  type        = string
}

variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string

  validation {
    condition     = can(regex("^(sbx|dev|qas|prd)$", var.environment))
    error_message = "Invalid input, options: \"sbx\", \"dev\", \"qas\", \"prd\"."
  }
}

variable "resource_instance_number" {
  default     = "001"
  description = "The resource instance number."
  type        = string

  validation {
    condition     = length(var.resource_instance_number) == 3
    error_message = "Must be a 3 character long resource_instance_number, e.g. 001."
  }

  validation {
    condition     = can(regex("^[0-9.]*$", var.resource_instance_number))
    error_message = "The 'resource_instance_number' value must be a valid and can only contain number characters from 0 to 9."
  }
}

variable "location" {
  default     =  "Germany Central"
  description = "The geographic location in which to deploy."
  type        = string
}

variable "team" {
  default     = "MG Innovators"
  description = "The team used for tagging resource groups and resources."
  type        = string
}

# Azure Container Registry
variable "number_of_container_registries" {
  default     = 1
  description = "The total number of Azure Container registries to deploy."
  type        = number
}

variable "acr_sku" {
  description = "SKU for the Azure Container Registry"
  type        = string
  default     = "Basic"
}

variable "acr_admin_enabled" {
  description = "Flag to enable admin user for the Azure Container Registry"
  type        = bool
  default     = true
}