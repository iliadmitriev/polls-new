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

# testing

## run tests 

1. run all tests
```shell
python3 manage.py test
```
2. run with keeping db in case of test fails
```shell
python3 manage.py test --keepdb
```
3. run all tests with details
```shell
python3 manage.py test --verbosity=2
```

## run tests with coverage

1. install coverage
```shell
pip install coverage
```
2. run with coverage
```shell
coverage run --source='.' manage.py test
```
3. print report with missing lines
```shell
coverage report -m
```
4. generate detailed html report
```shell
coverage html
open htmlcov/index.html
```

## tests parallel running for macOS

for macOS in order to tests work parallel you should use different settings file
```shell
python3 manage.py test --verbosity=2 --parallel --settings=mysite.settings-test-macos
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


# useful links

---
* admin http://127.0.0.1:8000/admin/
* polls http://127.0.0.1:8000/polls/
* api http://127.0.0.1:8000/api/
