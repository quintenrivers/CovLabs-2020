# CovLabs-2020
## Running `django_server`
```bash
cd django_server
mkdir venv
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt

python manage.py createsuperuser
# provide username, password, and email
# I recommend user: admin
#         password: password

python manage.py migrate core
python manage.py makemigrations
# sets up sqlite3 db

python manage.py runserver
# will run a server on localhost
```
## Using Admin Site
By going to the [admin site](http://localhost:8000/admin) you can log in with the superuser created. From here you can see users created and see the `Core` API which consists of `Visits`.

By clicking on the `Core` API link you can manually add visits or see the visits stored within the DB.

## API Root
With the server running, you can visit the [API Root](http://localhost:8000/api/) you can see all of the endpoints. All endpoints as of now, support standard [CRUD](https://www.codecademy.com/articles/what-is-crud). By clicking on a specific endpoint, you will be able to see the allowed operations as well as a form/buttons to perform the operations in the browser
