  EKS Nginx Deployment
This project demonstrates the deployment of an Nginx web server on an AWS EKS (Elastic Kubernetes Service) cluster using eksctl and kubectl. The deployment includes creating an EKS cluster, configuring networking, deploying Nginx, and exposing it via an AWS Load Balancer.

Project Overview
✔️ Created an EKS cluster (dev-cluster) with t2.micro instances.
✔️ Configured VPC, subnets, and enabled public IP assignment.
✔️ Manually created a managed node group (dev-nodes).
✔️ Deployed an Nginx application inside EKS.
✔️ Exposed Nginx using a LoadBalancer service for public access.
✔️ Verified successful deployment by accessing the LoadBalancer URL.
✔️ Deleted the EKS cluster to avoid costs.
✔️ Pushed the project to GitHub for documentation and future reference.

Project Files
📂 manifests/ → Kubernetes YAML manifests for Nginx deployment, service, and ingress.
📂 scripts/ → Python scripts for automating EKS deployments (future use).
