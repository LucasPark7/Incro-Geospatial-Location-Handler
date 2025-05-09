# Set namespace
$namespace = "default"

Write-Host "Deleting all Kubernetes resources in namespace '$namespace'..."
kubectl delete all --all -n $namespace

Write-Host "Deleting all PersistentVolumeClaims (PVCs)..."
kubectl delete pvc --all -n $namespace

Write-Host "Deleting all ConfigMaps and Secrets..."
kubectl delete configmap --all -n $namespace
kubectl delete secret --all -n $namespace

# Reapply your Kubernetes manifests
# Make sure these files exist in the current directory or update the paths
Write-Host "Reapplying manifests..."
kubectl apply -f .\k8s\kafka\zookeeper-deployment.yaml
kubectl apply -f .\k8s\kafka\kafka-deployment.yaml
kubectl apply -f .\k8s\postgis\postgis-deployment.yaml
kubectl apply -f .\k8s\backend-deployment.yaml
kubectl apply -f .\k8s\frontend-deployment.yaml

# Wait for all pods to be ready
Write-Host "Waiting for all pods to become ready..."
kubectl wait --for=condition=Ready pods --all -n $namespace --timeout=120s

Write-Host "App reboot complete."
