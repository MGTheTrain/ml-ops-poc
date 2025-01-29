# Azure Rg
variable "digital_product_affix" {
  default     = "mopocacr"
  description = "The digital product affix of the acr module."
  type        = string
}

variable "environment" {
  default     = "sbx"
  description = "The environment."
  type        = string
}

variable "resource_instance_number" {
  default     = "001"
  description = "The resource instance number."
  type        = string
}

variable "location" {
  default     = "West Europe"
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