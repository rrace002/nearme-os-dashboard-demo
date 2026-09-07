> For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.n8n.io/deploy/host-n8n.md).

# Host n8n

You can self-host n8n on your own infrastructure, on-premises, or in a private cloud, using Docker Compose, one-line setup, or other deployment methods. Not sure if self-hosting is right for you? See [Choose how to use n8n](/choose-how-to-use-n8n.md).

{% hint style="success" %}
**Don't want to read the docs? Run this:**

```bash
curl -fsSL https://get.n8n.io | sh
```

Requires Docker on Linux or macOS (or WSL on Windows). Sets up n8n locally in one step. See the [one-line setup guide](/deploy/host-n8n/install-options/one-line-setup.md) for what it does, or keep reading to compare every installation method.
{% endhint %}

All self-hosted installations use the same core product. Without a license key, n8n runs as the free Community edition. Adding a Business or Enterprise license key enables those editions. See [Compare editions](/deploy/host-n8n/community-edition-features.md) for the differences between the self-hosted editions.

## Choose your installation method <a href="#choose-your-installation-method" id="choose-your-installation-method"></a>

Select the installation method that best fits your technical requirements and infrastructure:

* **One-line setup**

  **Best for:** Quick setup with minimal configuration.

  **Requirements:** Linux or macOS system with curl installed.

  Automated installation script that handles all dependencies and configuration for you.

  [One-line setup guide](/deploy/host-n8n/install-options/one-line-setup.md)
* **Docker Compose**

  **Best for:** Production deployments with databases and additional services.

  **Requirements:** Docker and Docker Compose installed on your system.

  Multi-container setup ideal for robust deployments with persistent data and scalability.

  [Docker Compose guide](/deploy/host-n8n/install-options/install-using-docker-compose.md)
* **AWS**

  Deploy on Amazon Web Services using EC2, ECS, or other AWS services.

  [AWS setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws.md)
* **Azure**

  Host n8n on Microsoft Azure with container instances or virtual machines.

  [Azure setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure.md)
* **Google Cloud**

  Run n8n on Google Cloud using Cloud Run or Kubernetes Engine.

  [Google Cloud Run](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run.md) | [Kubernetes Engine](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md)
* **DigitalOcean**

  Simple droplet-based hosting ideal for small to medium deployments.

  [DigitalOcean setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean.md)
* **Hetzner**

  Cost-effective European hosting option with excellent performance.

  [Hetzner setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner.md)
* **Heroku**

  Platform-as-a-service option for quick deployment with minimal configuration.

  [Heroku setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku.md)
* **OpenShift**

  Enterprise Kubernetes platform for containerized applications.

  [OpenShift setup guide](/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc.md)
* **npm**

  **Best for:** Local development or testing.

  **Requirements:** Node.js installed on your system.

  npm installation is deprecated from n8n 3.0. Consider using Docker Compose or one-line setup instead.

  Installs n8n directly using Node Package Manager. Quick to set up but requires managing Node.js versions and dependencies yourself.

  [npm installation guide](/deploy/host-n8n/install-options/install-with-npm.md)
