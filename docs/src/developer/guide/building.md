---
title: GeoRepo-OS Building Guide
summary: GeoRepo is a UNICEF's geospatial web-based data storage and administrative boundary harmonization platform.
    - Tim Sutton
    - Dimas Tri Ciputra
    - Danang Tri Massandy
date: 2023-08-03
some_url: https://github.com/unicef-drp/GeoRepo-OS
copyright: Copyright 2023, Unicef
contact: georepo-no-reply@unicef.org
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#context_id: 1234
---


# Building the dev environment

This section covers the process of building and running the application from your IDE.

🚩 Make sure you have gone through the [IDE Setup Process](ide-setup.md) before following these notes.

Press `Ctrl -> P` 1️⃣ and then `>`and search for `Rebuild`. Select `Dev Containers: Rebuild and Reopen in Container`2️⃣. This will essentially mount your code tree inside a docker container and switch the development context of VSCode to be inside the container where all of the python etc. dependencies will be installed.

![image.png](img/building-1.png)

Once the task is running, a notification 1️⃣ will be shown in the bottom right of the VSCode window. Clicking in the notification will show you the setup progress 2️⃣. Note that this make take quite a while depending on the internet bandwidth you have and the CPU power of your machine.

![image.png](img/building-2.png)
## Open a dev container terminal

Open  terminal within the dev container context by clicking the `+`icon in the terminal pane 1️⃣. The new terminal 2️⃣ will show up in the list of running terminals 3️⃣

![image.png](img/building-3.png)

## Install FrontEnd libraries

```
cd /home/web/project/django_project/dashboard
npm install --legacy-peer-deps
```

![image.png](img/building-4.png)


## Run django migration

```
cd /home/web/project/django_project
python manage.py migrate
```
## Create super user

```
cd /home/web/project/django_project
python manage.py createsuperuser
```

During this process you will be prompted for your user name (defaults to root), email address and a password (which you need to confirm). Complete these as needed.

## Run the development server

Activate the Run and Debug tab 1️⃣ then select `Django + React` from the list of runners 3️⃣ and then press the Run icon 2️⃣. After doing this, the console should update indicate that the site can be opened at http://127.0.0.1:2000/

![image.png](img/running-1.png)

## Viewing your test instance

After completing the steps above, you should have the development server available on port 2000 of your local host:

```
http://localhost:2000
```

![image.png](img/running-2.png)

The site will be rather bare bones since it will need to be configured in the admin area to set up the theme etc.

🪧 Now that you have the built the project, move on to the [Design](design.md) documentation.