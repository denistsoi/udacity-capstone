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

---

GET /
- description: simple health check
- returns a status health check of the app

--- 
Resource Movies:

  
```
GET /movies  
```
(requires authorization header of `get:movies`)
- description: list of movies
- returns a list of movies

```
POST /movies  
```
(requires authorization header of `post:movies`)
- description: list of movies
- params: 
  - title: string
  - release_date: date

- returns status of created movie

```
PATCH /movies/<id>
```
(requires authorization header of `patch:movies`)
- description: updates movie
- params: 
  - title: string
  - release_date: date

- returns status of updated movie


```
DELETE /movies/</id>
```
(requires authorization header of `delete:movies`)
- description: deletes movie
- return status of deleted movie

---

Resource Actors:

```
GET /actors  
```
(requires authorization header of `get:actors`)
- description: list of actors
- returns a list of actors

```
POST /actors  
```
(requires authorization header of `post:actors`)
- description: list of actors
- params: 
  - name: string
  - age: number
  - gender: string

- returns status of created actor

```
PATCH /actors/<id>
```
(requires authorization header of `patch:actors`)
- description: updates actor
- params: 
  - name: string
  - age: number
  - gender: string

- returns status of updated actor


```
DELETE /actors/</id>
```
(requires authorization header of `delete:actors`)
- description: deletes actor
- return status of deleted actor



## author
Denis Tsoi <denistsoi@gmail.com>