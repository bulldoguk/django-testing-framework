# A Demo Django Project

To setup a project using Django and HTMX, including typing, testing, linting and critic feedback for developers to help keep them on the straight and narrow!

## Key libraries

Python - 3.11.3
Django - 4.2.3

## Basic setup

- Confirm that the key Django library is installed with `pip install django --update`
- From the root `repos/` folder, use Django to setup the basic folders with `django-admin startproject mysite`
- Add an application within the core site with `python manage.py startapp signup` from the `mysite` root folder
- Create the first view by editing the `mysite/signup/views.py` file
- Edit the `mysite/signup/urls.py` file to add this new url pattern
- In the top level `urls.py` file, add `path("signup/", include("signup.urls")),` to add this new app as a subfolder of the main website
- Create a `models.py` file in the `signup/` folder to start building your data model
-- Add that model to the project by adding the app to the installed apps list in the root `settings.py.`

### Black formatter
- Install with `pip install black`
- Reformat all files in the project with `black .`
- Check file formats (no changes made) with `black --check .`

### Mypy typing

Install mypy with `pip install mypy`
Use `/mypy.ini` to define common testing criteria across the whole project
Run `mypy` with `mypy <path-to-module> --config-file mypy.ini` to get a list of errors
In order to get sensible results with Django, need to also include `https://pypi.org/project/django-stubs/`
To prevent checking of migrations folders, add `exclude = migrations/` to mypy.ini
**To investigate** Setting `disallow_any_expr` in mypy.ini throws errors on almost every model definition

### Hypothesis and pytest
### Python critic

## Key commands

- Run the application in listen mode with `python manage.py runserver`
- Add new migrations with `python manage.py makemigrations polls`
- Update the DB migrations with `python manage.py migrate`


## References

- https://docs.djangoproject.com/en/4.2/intro/tutorial01/