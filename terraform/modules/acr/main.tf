resource "azurerm_resource_group" "this" {
  name     = "${var.digital_product_affix}-${var.environment}-rg${var.resource_instance_number}"
  location = var.location
  tags     = local.tags
}

resource "azurerm_container_registry" "this" {
  name                = local.container_registry_names[count.index]
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  sku                 = var.acr_sku
  admin_enabled       = var.acr_admin_enabled
  count               = var.number_of_container_registries
  tags                = local.tags
}