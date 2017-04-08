# Angular ES6 on Django Setup

This guide will take you through how to set up an Angular project using ES6 on a Django server.

## 1. Start a Django project.

`cd` into a directory where you'd like to store your code, then run:

```bash
$ django-admin startproject <project-name>
```

Next, we need to add an app to the project. We can do this by running:

```bash
$ cd <project-name>
$ django-admin startapp <app-name>
```

Your project directory should now look something like the following:

```
.
└── project
    ├── app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## 2. Add project configuration files to project root.

In the `project-config-files` folder in this repo, there are 3 items that need to be added to the project root.

* `.editorconfig`: Used to set editor rules so that formatting can remain uniform among multiple collaborators.
* `.gitignore`: Boilerplate for excluding some common folder/files from git.
* `.env`: This folder contains the files that will hold environment variables for separate environments of the project:

    | File | Environment | Description |
    |:---- |:----------- |:----- |
    | `.env` | N/A | Holds environment variables common to all environments. |
    | `.dev.env` | `development` | Holds environment variables necessary for local development. This file will be checked into git. |
    | `.dev.env.local` | `development` | An optional file for local development on a single computer. This file will NOT be checked into git. |
    | `.test.env` | `testing` | Holds environment variables necessary for deployment on a testing server. |
    | `.stage.env` | `staging` | Holds environment variables necessary for deployment on a staging server. |
    | `.prod.env` | `production` | Holds environment variables necessary for deployment on a production server. |

Your project directory should now look like this:

```
.
└── project
    ├── .editorconfig
    ├── .env
    │   ├── .dev.env
    │   ├── .dev.env.local
    │   ├── .env
    │   ├── .prod.env
    │   ├── .stage.env
    │   └── .test.env
    ├── .gitignore
    ├── app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```
