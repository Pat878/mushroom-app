# Mushroom project

```
git clone git@github.com:Pat878/mushroom-project.git
cd mushroom-project
pip install -r requirements.txt
```

If you don't have Django installed then run:

```
pip install Django
```

Create a `.env` file at the root of the project and add:

```
API_LINK=YOUR-API-LINK
```

Replace `YOUR-API-LINK` with the link you created when you set up AWS API.

Now you can start the project:

```
python manage.py runserver
```