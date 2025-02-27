from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Kubernetes API instance
api_instance = client.AppsV1Api()

def scale_deployment(namespace, deployment_name, replicas):
    """Scale the Nginx deployment to the desired number of replicas."""
    scaling_body = {"spec": {"replicas": replicas}}
    api_instance.patch_namespaced_deployment_scale(
        name=deployment_name, namespace=namespace, body=scaling_body
    )
    print(f"✅ Scaled {deployment_name} to {replicas} replicas.")

# Example usage: Scale to 3 replicas
scale_deployment(namespace="default", deployment_name="nginx-deployment", replicas=3)
