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
* `.env`: This folder contains the files that will hold environment variables for separate environments of the project.

    | File | Environment | Description |
    |:---- |:----------- |:----- |
    | `.env` | N/A | Holds environment variables common to all environments. |
    | `.dev.env` | `development` | Holds environment variables necessary for local development. This file will be checked into git. |
    | `.dev.env.local` | `development` | An optional file for defining custom variables on a single computer. This file will **NOT** be checked into git. |
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

## 3. Configure project settings.

Go into your `settings.py` file and mimic the example `project-settings/settings.py` file in this repo. Here are the most important changes:

- [x] Move the secret key into the `DJANGO_SECRET_KEY` environment variable in `.env`.
- [x] Add or remove necessary apps in `INSTALLED_APPS`.
- [x] Capture all the environment variables from your `.env` files.

    ```python
    DJANGO_ENV       = os.environ['DJANGO_ENV']
    SECRET_KEY       = os.environ['DJANGO_SECRET_KEY']
    APP_IP           = os.environ['APP_IP']
    APP_BACKEND_IP   = os.environ['APP_BACKEND_IP']
    APP_PSQL_DB_NAME = os.environ['APP_PSQL_DB_NAME']
    APP_PSQL_DB_HOST = os.environ['APP_PSQL_DB_HOST']
    APP_PSQL_DB_USER = os.environ['APP_PSQL_DB_USER']
    APP_PSQL_DB_PASS = os.environ['APP_PSQL_DB_PASS']
    APP_PSQL_DB_PORT = os.environ['APP_PSQL_DB_PORT']
    ```

- [x] Turn `DEBUG` on/off based on `DJANGO_ENV`.

    ```python
    if DJANGO_ENV == 'production':
        DEBUG = False
    else:
        DEBUG = True
    ```

- [x] Place `APP_IP` and `APP_BACKEND_IP` in `ALLOWED_HOSTS` array.

    ```python
    ALLOWED_HOSTS = [
        APP_IP,
        APP_BACKEND_IP
    ]
    ```

- [x] Switch your `DATABASES` engine to postgres, using the environment variables as the credentials.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': APP_PSQL_DB_NAME,
            'USER': APP_PSQL_DB_USER,
            'PASSWORD': APP_PSQL_DB_PASS,
            'HOST': APP_PSQL_DB_HOST,
            'PORT': APP_PSQL_DB_PORT
        }
    }
    ```

- [x] Route the `/static/` url to your `static` directory (which doesn't exist yet, but will in a moment).

    ```python
    STATIC_DIR = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = [
        STATIC_DIR,
    ]

    STATIC_URL = '/static/'
    ```

## 4. Set up your first route.

In `<project>/<project>/urls.py`, add the following code:

```python
from django.conf.urls import include#, url
# from django.contrib import admin

urlpatterns = [
    # (optional) you can keep the admin route if you're going to use it
    # otherwise, go ahead and delete it
    # url(r'^admin/', admin.site.urls),
    url(r'^', include('amb_app.urls')),
]
```

Then, in `<project>/<app>/`, create a `urls.py` file and add the following code:

```python
from django.conf.urls import url
from <app> import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
```

Lastly, in your `views.py` file, set up the `index` view:

```python
from django.shortcuts import render
from django.http import JsonResponse

import os
import json

def index(request):
    root                = os.path.dirname(os.path.abspath(__file__))
    webpack_assets_path = os.path.join(root, 'webpack-assets.json')

    with open(webpack_assets_path) as webpack_assets_file:
        assets = json.load(webpack_assets_file)

    return render(request, 'index.html', { 'assets': assets })
```

Don't worry about the `webpack-assets.json` file for now. It will be auto-generated later on.

## 5. Initialize your app as a `node` module.

In order to take advantage of front-end dev tools like `Webpack2` and `Gulp`, we need set up our `<app>` root folder as a `node` module. Normally you would use `npm` for this, but I'm going to use `yarn` here instead. You could do the same thing with `npm`, but `yarn` makes it easier to freeze version numbers across different environments.

In your `<app>` folder, run:

```bash
$ yarn init
```

Go through all the questions until you reach the end. A `package.json` file should have been generated that looks something like this:

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "Example app.",
  "main": "index.js",
  "author": "m-amaya",
  "license": "MIT"
}
```

Next, we're going to install all of our dependencies in one go:

```bash
$ yarn add angular angular-animate angular-cookies angular-nvd3 angular-ui-router assets-webpack-plugin babel-core babel-loader babel-preset-es2015 compression-webpack-plugin css-loader d3@^3.4.4 del extract-text-webpack-plugin gulp html-loader jquery ng-annotate-loader ng-lodash node-sass normalize.css nvd3 postcss-loader sass-loader socket.io-client uglify-js uglifyjs-webpack-plugin webpack webpack-stream
```

Your `package.json` should now have a list of all these dependencies. All of these dependencies should have been installed in the `node_modules` folder. And, a `yarn.lock` file should have been generated that locks down the dependency versions.

Before we move on to generating our Angular app, let's compare project directories:

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
    |   ├-- node_modules
    │   ├── package.json
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── yarn.lock
    ├── manage.py
    └── project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```
