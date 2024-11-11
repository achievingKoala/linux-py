cluster_info_commands = [
    {"command": "kubectl cluster-info", "description": "Display cluster information"},
    {"command": "kubectl get nodes", "description": "List all nodes in the cluster"},
    {"command": "kubectl get namespaces", "description": "List all namespaces in the cluster"},
    {"command": "kubectl config get-contexts", "description": "List available contexts"},
    {"command": "kubectl config use-context context_name", "description": "Switch to the specified context"}
]

pod_management_commands = [
    {"command": "kubectl get pods", "description": "List all pods in the current namespace"},
    {"command": "kubectl get pods --all-namespaces", "description": "List all pods across all namespaces"},
    {"command": "kubectl describe pod pod_name", "description": "Show detailed information about a pod"},
    {"command": "kubectl logs pod_name", "description": "View the logs of a pod"},
    {"command": "kubectl logs pod_name -c container_name", "description": "View the logs of a specific container in a pod"},
    {"command": "kubectl exec -it pod_name -- /bin/sh", "description": "Execute a command in a pod (e.g., open a shell)"}
]

deployment_management_commands = [
    {"command": "kubectl create deployment nginx --image=nginx", "description": "Create a deployment with the nginx image"},
    {"command": "kubectl get deployments", "description": "List all deployments in the current namespace"},
    {"command": "kubectl describe deployment deployment_name", "description": "Show detailed information about a deployment"},
    {"command": "kubectl delete deployment deployment_name", "description": "Delete a deployment"}
]

service_management_commands = [
    {"command": "kubectl expose deployment nginx --type=NodePort --port=80", "description": "Expose a deployment as a NodePort service"},
    {"command": "kubectl get services", "description": "List all services in the current namespace"},
    {"command": "kubectl describe service service_name", "description": "Show detailed information about a service"},
    {"command": "kubectl delete service service_name", "description": "Delete a service"}
]

config_and_secret_management_commands = [
    {"command": "kubectl create configmap my-config --from-file=config.txt", "description": "Create a ConfigMap from a file"},
    {"command": "kubectl get configmaps", "description": "List all ConfigMaps in the current namespace"},
    {"command": "kubectl describe configmap my-config", "description": "Show detailed information about a ConfigMap"},
    {"command": "kubectl delete configmap my-config", "description": "Delete a ConfigMap"},
    {"command": "kubectl create secret generic my-secret --from-literal=password=YOUR_PASSWORD", "description": "Create a Secret"},
    {"command": "kubectl get secrets", "description": "List all Secrets in the current namespace"},
    {"command": "kubectl describe secret my-secret", "description": "Show detailed information about a Secret"},
    {"command": "kubectl delete secret my-secret", "description": "Delete a Secret"}
]

resource_management_commands = [
    {"command": "kubectl apply -f config.yaml", "description": "Apply a configuration file to create or update resources"},
    {"command": "kubectl delete -f config.yaml", "description": "Delete resources defined in a configuration file"},
    {"command": "kubectl get all", "description": "List all resources in the current namespace"},
    {"command": "kubectl scale deployment nginx --replicas=3", "description": "Scale a deployment to 3 replicas"},
    {"command": "kubectl autoscale deployment nginx --min=2 --max=5 --cpu-percent=80", "description": "Set up autoscaling for a deployment"}
]

advanced_debugging_commands = [
    {"command": "kubectl top nodes", "description": "Display resource usage for nodes"},
    {"command": "kubectl top pods", "description": "Display resource usage for pods"},
    {"command": "kubectl describe node node_name", "description": "Show detailed information about a node"},
    {"command": "kubectl get events", "description": "List events in the cluster"},
    {"command": "kubectl get pod pod_name -o yaml", "description": "Display the YAML definition of a pod"}
]

# {"command": "curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash", "description": "Install k3d tool for managing K3s clusters in Docker"},