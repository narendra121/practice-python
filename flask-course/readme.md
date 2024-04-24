pip install pipenv

pipenv install

pipenv shell

pipenv install flask

 export FLASK_APP=hello

 flask run

 export FLASK_ENV=development
export FLASK_ENV=development && flask run
export FLASK_DEBUG=1 && flask run

 export FLASK_APP=urlshort

 pipenv install pytest

 pipenv install gunicorn

 wsgi


 gunicorn "urlshort:create_app()" -b 0.0.0.0 --daemon

 sudo apt install nginx

 systemctl status nginx

 sudo nano /etc/nginx/sites-enabled/default



 jinja