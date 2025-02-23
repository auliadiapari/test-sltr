# Cloud Infra GCP

Illustrated with a broader view from Organization > Project > Resources level, the common implementation is using host-project & shared VPC

## CI/CD

- The CI process is quite simple, started from Code commit after changes, Github actions will build the image and push it to the dockerhub repository or we can use artifact registry in GCP instead
- The CD process is expected via SSH, it's being set up to having the SSH to Bastion VM/Jumphost that already connected to GKE cluster, which is the GKE cluster should be isolated, the one can only having the control plane communication is to the Bastion VM.
- After the SSH, it will set having kubectl command to set the image version as desired/purposed/expected, and will continue executing restart rollout to the specified deployment.

Notes: we can leverage using CD tools such as, ArgoCD to automate the CD process, the CI should be just after the whole process of CI (Build, Test, image versioning and push to image repo)


## GCP Infra

Assuming the the GKE cluster is already being provisioned.

- Configmap is being used to store environment variable, just a port number
- Deployment will create 2 replcas of pod, with resource requrest & limits defined, or we could leverage Horizontal pod autoscaler to manage the replicaset. Configmap is mounted to this kubernetes object
- Service object type is using ClusterIP, its easier to scale if we having more services to connect with
- Ingress is using GCE Ingress, which is platform native ingress provider, we could leverage all of needed/purposed annotations for all GCP related services as i made, it will spin up the Application load balancing in GCP, configurated using managed certificate by GCP, disabling http, and static external ip

Notes: its better to use the platform managed certificates to easier set up and maintain, combined with GCP/GCE Ingress, but if decided to use Custome ingress controller such as NGINX, we can choose or consider use the Letsencrypt if another approach decided

