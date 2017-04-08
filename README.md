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

- [ ] Move the secret key into the `DJANGO_SECRET_KEY` environment variable in `.env`.
- [ ] Capture all the environment variables from your `.env` files.

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

- [ ] Turn `DEBUG` on/off based on `DJANGO_ENV`.

    ```python
    if DJANGO_ENV == 'production':
        DEBUG = False
    else:
        DEBUG = True
    ```

- [ ] Place `APP_IP` and `APP_BACKEND_IP` in `ALLOWED_HOSTS` array.

    ```python
    ALLOWED_HOSTS = [
        APP_IP,
        APP_BACKEND_IP
    ]
    ```

- [ ] Add or remove necessary apps in `INSTALLED_APPS`.
- [ ] Switch your `DATABASES` engine to postgres, using the environment variables as the credentials.

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

- [ ] Route the `/static/` url to your `static` directory (which doesn't exist yet, but will in a moment).

    ```python
    STATIC_DIR = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = [
        STATIC_DIR,
    ]

    STATIC_URL = '/static/'
    ```
