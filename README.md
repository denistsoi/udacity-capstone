# capstone project

## description

Udacity Fullstack capstone project


### Getting Started


```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py db init
python manage.py db migrate

FLASK_APP=app.py flask run
```

### running tests

```
python test_app.py
```

### hosted heroku app

https://udacity-fullstack-capstone.herokuapp.com/


### Tokens

Authentication is done via Auth0 
Login with the following:

Url
  
`https://dev-98w9-5eh.auth0.com/authorize?audience=agency&response_type=token&client_id=eG5AKHAYrvf1jToGgKbBwUdmIdaVDWbd&redirect_uri=http://localhost:5000`

Example accounts

casting_assistant@example.com   
#m5V@ccgFMO7

casting_director@example.com   
7a03jR%F6R1d
  
executive_producer@example.com 
  1CU1OJppfe0$

tokens can be found in `test_app.py` for validating tests


## endpoints

/movies



## author
Denis Tsoi <denistsoi@gmail.com>