# Azure Rg
variable "digital_product_affix_sa" {
  default     = "gftfbe"
  description = "The digital product affix of the Storage Account module."
  type        = string
}

variable "digital_product_affix_acr_module" {
  default     = "mlopsftwcr"
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
  default     = "Switzerland North"
  description = "The geographic location in which to deploy."
  type        = string
}

variable "team" {
  default     = "MG Innovators"
  description = "The team used for tagging resource groups and resources."
  type        = string
}

# Azure Container Registry
variable "number_of_storage_accounts" {
  default     = 1
  description = "The total number of Azure Storage Accounts to deploy."
  type        = number
}

variable "sa_account_tier" {
  description = "Account tier for the Azure Storage Account"
  type        = string
  default     = "Standard"
}

variable "sa_account_replication_type" {
  description = "Account replication type for the Azure Storage Account"
  type        = string
  default     = "LRS"
}

variable "sc_container_access_type" {
  default     = "private"
  description = "Container access type of the Storage Account Container"
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