# Known issues

## CoreDNS nslookup error

If the following error occurs in custom training jobs with apps that use components to communicate with external systems for uploading blobs, such as the [mnist keras training app](./python/keras-mnist-training/), refer to the details below:

```sh
;; Got recursion not available from 10.0.0.10
;; Got recursion not available from 10.0.0.10
;; Got recursion not available from 10.0.0.10
;; Got recursion not available from 10.0.0.10
Server:         10.0.0.10
Address:        10.0.0.10#53

** server can't find mopoctbsbxsac001.blob.core.windows.net: NXDOMAIN
```

the CoreDNS ConfigMap needs to be edited to enable recursion trough `kubectl edit cm coredns -n kube-system` and adding following entry

```sh
header {
  response set ra
}
```

You might also want to review the CoreDNS ConfigMap in the deployed AKS view within the Azure Portal Web UI. 

![CoreDNS config map edited](./images/core-dns-configmap-edited.jpg)
![CoreDNS config map in Azure Portal](./images/core-dns-config-map-in-azure-portal.jpg)

You can also refer to this link for further guidance: https://jbn1233.medium.com/kubernetes-kube-dns-fix-nslookup-error-got-recursion-not-available-from-ff9ee86d1823. 

You can optionally review the outbound ports in the network security group associated with your VNet and consider adding a rule to allow outbound traffic on port 443.

![NSG Outbound ports rule](./images/nsg-outbound-ports-rule.jpg)
![NSG Outbound ports rule results](./images/nsg-outbound-ports-rule-results.jpg)

## KServe v0.7.0 installation error

When running `kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.7.0/kserve.yaml -n kserve` following error logs appears:

```sh
...
resource mapping not found for name: "serving-cert" namespace: "kserve" from "https://github.com/kserve/kserve/releases/download/v0.7.0/kserve.yaml": no matches for kind "Certificate" in version "cert-manager.io/v1alpha2"
ensure CRDs are installed first
resource mapping not found for name: "selfsigned-issuer" namespace: "kserve" from "https://github.com/kserve/kserve/releases/download/v0.7.0/kserve.yaml": no matches for kind "Issuer" in version "cert-manager.io/v1alpha2"
ensure CRDs are installed first
```

It works with v0.9.0 using the command `kubectl apply -f "https://github.com/kserve/kserve/releases/download/v0.9.0/kserve.yaml"`:

```sh
namespace/kserve unchanged
customresourcedefinition.apiextensions.k8s.io/clusterservingruntimes.serving.kserve.io configured
customresourcedefinition.apiextensions.k8s.io/inferencegraphs.serving.kserve.io configured
customresourcedefinition.apiextensions.k8s.io/inferenceservices.serving.kserve.io configured
customresourcedefinition.apiextensions.k8s.io/servingruntimes.serving.kserve.io configured
customresourcedefinition.apiextensions.k8s.io/trainedmodels.serving.kserve.io configured
serviceaccount/kserve-controller-manager created
role.rbac.authorization.k8s.io/kserve-leader-election-role created
clusterrole.rbac.authorization.k8s.io/kserve-manager-role configured
clusterrole.rbac.authorization.k8s.io/kserve-proxy-role unchanged
rolebinding.rbac.authorization.k8s.io/kserve-leader-election-rolebinding created
clusterrolebinding.rbac.authorization.k8s.io/kserve-manager-rolebinding configured
clusterrolebinding.rbac.authorization.k8s.io/kserve-proxy-rolebinding configured
configmap/inferenceservice-config configured
configmap/kserve-config unchanged
secret/kserve-webhook-server-secret unchanged
service/kserve-controller-manager-metrics-service unchanged
service/kserve-controller-manager-service configured
service/kserve-webhook-server-service unchanged
deployment.apps/kserve-controller-manager created
statefulset.apps/kserve-controller-manager configured
certificate.cert-manager.io/serving-cert created
issuer.cert-manager.io/selfsigned-issuer created
mutatingwebhookconfiguration.admissionregistration.k8s.io/inferenceservice.serving.kserve.io configured
validatingwebhookconfiguration.admissionregistration.k8s.io/inferencegraph.serving.kserve.io configured
validatingwebhookconfiguration.admissionregistration.k8s.io/inferenceservice.serving.kserve.io configured
validatingwebhookconfiguration.admissionregistration.k8s.io/trainedmodel.serving.kserve.io configured
```