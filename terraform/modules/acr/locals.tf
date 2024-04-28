locals {
  tags = {
    env         = "${var.environment}",
    team        = "${var.team}",
    owner       = "MGTheTrain",
    project     = "helm-chart-samples-ftw",
    app-purpose = "Deployment of an Azure Container Registry",
    Stage       = "${var.environment}"
  }
  container_registry_names = [for i in range(var.number_of_container_registries) : format("%s%ssa%03d", var.digital_product_affix, var.environment, i + 1)]
}