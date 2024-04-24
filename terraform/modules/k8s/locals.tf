locals {
  tags = {
    env     = "${var.environment}",
    project = "ml-ops-ftw",
    Stage   = "${var.environment}"
  }
}