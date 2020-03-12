travel demo project with Flask
==================
[![Heroku](https://heroku-badge.herokuapp.com/?app=stepik-travel-project&style=flat)](https://stepik-travel-project.herokuapp.com)

##### features:
 - index page for show random 6 tours
 - direction page for show tour by direction
 - tour page for show tour detail
 
##### requirements:
 - Python 3.5+
 - Flask 1.1.1
 - Gunicorn 20.0.4

##### install requirements:
`pip3 install -r requirements.txt`

##### run app:
 - run `gunicorn 'wsgi:app'`
 - open default page http://127.0.0.1:8000
