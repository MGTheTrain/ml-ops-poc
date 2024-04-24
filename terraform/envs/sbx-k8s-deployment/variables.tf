variable "digital_product_affix" {
  default     = "gitopsftw"
  description = "The digital product affix."
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

variable "virtual_network_address_space" {
  type        = list(string)
  default     = ["10.1.0.0/16"]
  description = "The virtual network address space. E.g. 2^(32-16)=65536 private ips in Vnet."
}

variable "number_of_aks" {
  default     = 1
  description = "The total number of AKses to deploy."
  type        = number
}

variable "aks_admin_username" {
  type        = string
  default     = "azureuser"
  description = "The AKS admin username"
}

variable "aks_enable_auto_scaling" {
  type        = bool
  default     = true
  description = "Whether to allow the AKS cluster to automatically adjust the number of nodes in a node pool"
}

variable "aks_node_count" {
  type        = number
  default     = 1
  description = "The AKS node count"
}

variable "aks_max_node_count" {
  type        = number
  default     = 2
  description = "The AKS max node count"
}

variable "aks_vm_size" {
  type        = string
  default     = "Standard_B2s"
  description = "The AKS vm size. Other option is Standard_B2s. See https://learn.microsoft.com/en-us/azure/virtual-machines/sizes, https://azureprice.net/"
}

variable "aks_os_disk_size_gb" {
  type        = string
  default     = "128"
  description = "The AKS Agent Operating System disk size in GB"
}