# install

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
6. run
```shell
python3 manage.py runserver 0:8000
```