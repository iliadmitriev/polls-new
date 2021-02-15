# install

---

1. install python3 and create virtual env
```shell
python3 -m venv venv
source venv/bin/activate
```
2. install requirements
```shell
pip install -r requirements.txt
```
3. create a db (run migrations)
```shell
python3 manage.py migrate
```
4. compile messages
```shell
python3 manage.py compilemessages
```
5. create superuser
```shell
python3 manage.py createsuperuser
```

# development

---
1. set environment variables
```shell
DJANGO_DEBUG=True
```

2. make migrations and migrate
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

3. make messages
```shell
python3 manage.py makemessages -a
python3 manage.py compilemessages
```

4. run
```shell
python3 manage.py runserver 0:8000
```

# production

---

## prepare

1. migrate
```shell
python3 manage.py migrate --noinput
```

2. collect static
```shell
python3 manage.py collectstatic --noinput
```

3. compile messages
```shell
python3 manage.py compilemessages
```

## Web server

### uWSGI

1. install uWSGI
```shell
pip install uWSGI
```

2. Run
```shell
uwsgi --ini uwsgi.ini
```

### gunicorn

1. install
```shell
pip install gunicorn
```
2. run
```shell
gunicorn --bind :8000 --workers 4 --threads 8 --timeout 0 mysite.wsgi
```


# usefull links

---
* admin http://127.0.0.1:8000/admin/
* polls http://127.0.0.1:8000/polls/
* api http://127.0.0.1:8000/api/
