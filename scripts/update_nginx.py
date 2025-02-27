from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Kubernetes API instance
api_instance = client.AppsV1Api()

def update_deployment_image(namespace, deployment_name, new_image):
    """Update the Nginx deployment to use a new image."""
    patch_body = {
        "spec": {
            "template": {
                "spec": {
                    "containers": [
                        {"name": "nginx", "image": new_image}
                    ]
                }
            }
        }
    }
    api_instance.patch_namespaced_deployment(
        name=deployment_name, namespace=namespace, body=patch_body
    )
    print(f"✅ Updated {deployment_name} to use image {new_image}")

# Example usage: Update to Nginx 1.21
update_deployment_image(namespace="default", deployment_name="nginx-deployment", new_image="nginx:1.21")
