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

To give a brief overview, everything in CapRover is in a container, including NGINX, so no container can access other container data. But if you want to serve your media files (this will work the same for static files), NGINX needs to be able to access these files. Fortunately, the NGINX CapRover container provides a folder on the host that it can read and can be shared with other containers. So, basically, what you need to do is tell your Django app to write the media files in this shared folder so that NGINX can read them.

```python
# Django media settings
STORAGES = {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
}
MEDIA_ROOT = APPS_DIR / "media"
MEDIA_URL = "/media/"
```

Some assumptions:
- The project is named `myjourney` (this is also the `APPS_DIR`).
- In the project's running container, the project is in a folder `/app`, so the media files would be located in `/app/myjourney/media`.

The NGINX container in CapRover provides a shared folder for apps to store data that it can access. Check [here](https://caprover.com/docs/nginx-customization.html#custom-files-and-directories) for more details.
- On the host: `/captain/data/nginx-shared`
- In the container: `/nginx-shared`

1. Create a media folder for `myjourney` on the host in the shared folder, so something like `/captain/data/nginx-shared/myjourney/media`.
2. Add a persistent directory in the app config in CapRover. This will map the media app in your container to the media directory in the CapRover shared directory on the host.
   - **Path in App**: `/app/myjourney/media`
   - **Path on Host** (don't let CapRover manage the path): `/captain/data/nginx-shared/myjourney/media`
3. Configure your app's NGINX to serve the files from the NGINX shared folder when requests are received to the media path.
   ```text
   location /media/ {
       alias /nginx-shared/myjourney/media/;
   }
   ```
   Update both server configurations with this change.
