---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pull Container Images with A License

Cohere provides access to container images through a registry authenticated with a license. Users can pull these images and replicate them in their environment, as needed, to avoid runtime network access from inside the cluster.

Images will come through the `proxy.replicated.com` registry. Pulling the images will require firewall access open to `proxy.replicated.com` and `proxy-auth.replicated.com`. More information on these endpoints may be found [here](https://docs.replicated.com/enterprise/installing-general-requirements#firewall-openings-for-online-installations).

To test pulling images with a license, modify your docker CLI configuration to include authentication details for the registry. Note: `docker login` will not work.

The docker CLI is only an example; any tool which can pull images with credentials will work with the license ID configured as both username and password. Skopeo is another popular tool for copying images between registries which will work with this flow.

>   **ℹ️ Info**
>
> The following commands will overwrite your existing docker CLI configuration with authentication details for Cohere’s registry. If preferred, you can manually add the authentication details to preserve your existing configuration.
```
LICENSE_ID="<YOUR LICENSE ID>"

cat <<EOF > ~/.docker/config.json 
{
    "auths": {
        "proxy.replicated.com": {
            "auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"
        }
    }
}
EOF
```typescript
If you prefer to update your docker CLI configuration only for the current terminal session you can export an environment variable instead:
```
LICENSE_ID="<YOUR LICENSE ID>"

export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json"
{
    "auths": {
        "proxy.replicated.com": {
            "auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"
        }
    }
}
EOF
```
Validate that the authenticated image pull works correctly using the docker CLI:
```
CUSTOMER_TAG=image_tag_from_cohere # provided by Cohere

docker pull $CUSTOMER_TAG
```
You can now re-tag and replicate this image anywhere you want, using workflows appropriate to your air-gapped environment.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
