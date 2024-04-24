output "ml_ops_ftw_namespace" {
  value = kubernetes_namespace.ml_ops_ftw_namespace.metadata.0.name
}