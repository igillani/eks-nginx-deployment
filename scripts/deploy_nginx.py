from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Create Kubernetes API clients
api_instance = client.AppsV1Api()

# Define deployment YAML
deployment = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {"name": "nginx-deployment"},
    "spec": {
        "replicas": 2,
        "selector": {"matchLabels": {"app": "nginx"}},
        "template": {
            "metadata": {"labels": {"app": "nginx"}},
            "spec": {
                "containers": [{
                    "name": "nginx",
                    "image": "nginx:latest",
                    "ports": [{"containerPort": 80}]
                }]
            }
        }
    }
}

# Deploy Nginx
api_instance.create_namespaced_deployment(namespace="default", body=deployment)
print("✅ Nginx deployment created successfully!")