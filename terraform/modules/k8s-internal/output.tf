output "internal_apps_namespace" {
  value = kubernetes_namespace.internal_apps.metadata.0.name
}