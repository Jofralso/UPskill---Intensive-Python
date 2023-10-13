
Here's a brief overview of how Django templates work and how you can use them to display information:

1. **Template Syntax:**
   Django templates use a special syntax for inserting dynamic content:
   - `{{ variable }}`: Displays the value of a variable.
   - `{% tag %}`: Executes control flow logic or other operations.
   - `{# comment #}`: Adds comments within the template.

2. **Displaying Variables:**
   You can display variables by using double curly braces `{{ variable }}` within your HTML template. For example:
   ```html
   <p>Hello, {{ user.username }}!</p>
   ```

3. **Control Flow and Logic:**
   You can use template tags like `{% if %}`, `{% for %}`, `{% else %}`, `{% endif %}`, etc., to control the flow of your template based on conditions and iterate over data.

4. **Inclusion and Extending:**
   You can include other templates using `{% include 'template_name.html' %}` or extend a base template using `{% extends 'base.html' %}`.

5. **Filters:**
   Filters allow you to modify the output of a variable. For example, `{{ value|filter_name }}`.

6. **Templatetags:**
   Django allows you to create custom templatetags to extend the functionality of templates.

7. **Comments:**
   You can add comments using `{# This is a comment #}`.

8. **Template Inheritance:**
   Templates can inherit from a base template and override specific blocks using `{% block %}` and `{% extends %}`.

Here's a simple example of a Django template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Webpage</title>
</head>
<body>
    <h1>Hello, {{ user.username }}!</h1>
    
    {% if user.is_authenticated %}
        <p>Welcome back, {{ user.first_name }}!</p>
    {% else %}
        <p>Please log in to access your account.</p>
    {% endif %}
</body>
</html>
```

In this example, the template displays a greeting based on whether the user is authenticated or not.

Django templates are a powerful tool for creating dynamic and interactive web pages by integrating Python logic into your HTML. You can use them to display various types of information based on your application's requirements.


----
To reset all tables in Django, you'll need to delete all records in each table and then recreate the database schema. Here's a step-by-step approach to achieve this:

1. **Delete all records from all tables:**

   First, delete all records from each table in your Django application. You can use Django's ORM to achieve this.

   ```python
   # Import your models
   from myapp.models import Employee, Contact, Department

   # Delete records from each table
   Employee.objects.all().delete()
   Contact.objects.all().delete()
   Department.objects.all().delete()
   ```

   Replace `myapp` with the actual name of your Django app, and adjust the model names accordingly.

2. **Generate a new migration to drop tables:**

   Run the following command to generate a new migration that drops the tables:

   ```bash
   python manage.py makemigrations --empty yourapp
   ```

   Replace `yourapp` with the actual name of your Django app.

3. **Edit the generated migration:**

   Open the generated migration file (located in `yourapp/migrations/`) and modify it to drop the tables. It should look something like this:

   ```python
   from django.db import migrations

   def drop_tables(apps, schema_editor):
       # Drop tables
       YourModel = apps.get_model('yourapp', 'YourModel')
       YourModel.objects.all().delete()

   class Migration(migrations.Migration):

       dependencies = [
           # Add any dependencies here if needed
       ]

       operations = [
           migrations.RunPython(drop_tables),
       ]
   ```

   Replace `YourModel` with the actual model you want to reset.

4. **Apply the migration:**

   Apply the migration to drop the tables:

   ```bash
   python manage.py migrate yourapp
   ```

   Replace `yourapp` with the actual name of your Django app.

5. **Generate and apply new migrations:**

   After dropping the tables, generate and apply new migrations for each app to recreate the schema and reset the primary key sequence:

   ```bash
   python manage.py makemigrations yourapp1
   python manage.py makemigrations yourapp2
   # ... and so on for each app in your project
   ```

   Replace `yourapp1`, `yourapp2`, etc., with the actual names of your Django apps.

   ```bash
   python manage.py migrate
   ```

   This will recreate the tables and reset the primary key sequence.

By following these steps, you'll effectively recreate the tables and reset the primary key sequence for your models. Always ensure you have proper backups and are prepared for the loss of data before proceeding.