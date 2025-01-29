output "external_services_namespace" {
  value = kubernetes_namespace.external_services.metadata.0.name
}