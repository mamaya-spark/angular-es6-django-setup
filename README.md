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

Your file tree should now look something like the following:

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
