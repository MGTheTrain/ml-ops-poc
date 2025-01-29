locals {
  tags = {
    env     = "${var.environment}",
    project = "ml-ops-poc",
    Stage   = "${var.environment}"
  }
}