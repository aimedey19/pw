---
share: true
featured: true
title: Media Setup for CapRover NGINX and Django
slug: media_setup_for_caprover_nginx_and_django
tags:
 - django
 - caprover
 - devops
description: This guide explains how to configure NGINX on CapRover to serve media files for a Django project by setting up a shared folder accessible by both the NGINX and Django containers.
publish_date: 2025-01-12
upload_path: posts
---

### Overview

Since CapRover uses containers for all services, including NGINX, containers cannot access each other’s data directly.
To serve media files, NGINX needs access to them. However, if your Django project is configured to use file storage, it will store files inside its container (or a volume, depending on your configuration).
The solution is to use a shared folder that both containers can access:

1. The NGINX container provides a shared folder located at `/nginx-shared`.
2. By configuring Django to write media files into this shared folder, NGINX can serve them.

An advantage of this solution is that it is similar to using a volume, meaning you will not lose your media files when the container is restarted.

### Step 1: Update Django Media Settings

Add or update the following settings in your `settings.py` file:

```python
# Django media settings
STORAGES = {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
}
MEDIA_ROOT = APPS_DIR / "media"
MEDIA_URL = "/media/"
```

**Assumptions**:
- The project name is `myjourney` (also the `APPS_DIR`).
- In the running container, the project resides in `/app`, so media files are located in `/app/myjourney/media`.

### Step 2: Use the CapRover Shared Directory

CapRover’s NGINX container offers a shared folder for storing data accessible by other containers(Check [here](https://caprover.com/docs/nginx-customization.html#custom-files-and-directories) for more details.):
- **Host Path**: `/captain/data/nginx-shared`
- **Container Path**: `/nginx-shared`

#### 1. Create the Media Directory

On the host, create a media folder in the shared directory: `/captain/data/nginx-shared/myjourney/media`

#### 2. Configure CapRover to Use the Shared Directory

In CapRover’s app configuration, set up a persistent directory:

- **Path in App**: `/app/myjourney/media`
- **Path on Host**: `/captain/data/nginx-shared/myjourney/media`

> *Note*: Do not let CapRover manage this path automatically.

### Step 3: Update NGINX Configuration

Add a `location` block to serve media files from the shared folder:

```nginx
location /media/ {
    alias /nginx-shared/myjourney/media/;
}
```

Be sure to update the configuration in both your NGINX servers.

And that’s it! Your Django project should now be able to serve media files using NGINX. 🚀
