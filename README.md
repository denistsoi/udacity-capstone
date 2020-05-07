# capstone project

## description

Udacity Fullstack capstone project


### Motivation

This aims to consolidate the knowledge gained from the nanodegree.  

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
  

Aims:
1. Create data models representing `Movies`, `Actors` in `models.py`.  
2. use `auth.py` to verify permissions of the user role.  
3. perform database migrations.  
4. API flask server for `CRUD` in `app.py`  
5. Automated tests in `test_app.py`  
6. deploy application to heroku.  

### Getting Started


```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

source ./setup.sh

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

tokens can be found in `setup.sh`


## Roles

1. Casting assistant:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`

Casting Director:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`
- update actors `PATCH /actors (update:actors)`
- update movies `PATCH /movies (update:movies)`
- add actors `POST /actors (post:actors)`
- remove actors `DELETE /actors (delete:actors)`

Executive Producer:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`
- update actors `PATCH /actors (update:actors)`
- update movies `PATCH /movies (update:movies)`
- add actors `POST /actors (post:actors)`
- remove actors `DELETE /actors (delete:actors)`
- add movies `POST /movies (post:movies)`
- remove movies `DELETE /movies (delete:movies)`

## endpoints

---

```
GET /
```
- description: simple health check
- request arguments: `None`
- returns a status health check of the app

--- 
Resource Movies:

  
```
GET /movies  
```

- description: list of movies
- required-permission: `get:movies`
- request arguments: None
- returns: list of movies
```
{
    "success": True,
    "movies": [{ 
      id: 1,
      title: "Titanic", 
      release_date: "Thu, 07 May 2020 00:00:00 GMT"
    }]
}
```

---

```
POST /movies  
```
- description: creates movies
- required-permission: `post:movies`
- request arguments: 
  - title (required): `string`
  - release_date (required): `string`

- returns: status and data of newly created movie
```
{
    "success": True,
    "movies": [{ 
      id: 2,
      title: "Cats", 
      release_date: "Sun, 03 May 2020 00:00:00 GMT"
    }]
}
```

---

```
PATCH /movies/<id>
```
- description: updates movie
- required-permission: `patch:movies`
- request arguments: 
  - title (optional): `string`
  - release_date (optional): `date`

- returns status of updated movie
```
{
    "success": True,
    "movies": [{ 
      id: 2,
      title: "Bob", 
      release_date: "Sun, 03 May 2020 00:00:00 GMT"
    }]
}
```

---

```
DELETE /movies/<id>
```
- description: deletes movie
- required-permission: `delete:movies`
- request arguments: None
- return status of deleted movie
```
{
    "success": True,
    "delete": 2
}
```

---

Resource Actors:

```
GET /actors  
```
- description: list of actors
- required-permission: `get:actors`
- request arguments: None
- returns a list of actors

```
{
    "success": True,
    "actors": [{ 
      id: 1,
      name: "Bob", 
      age: 25,
      gender: "Male"
    }]
}
```

---

```
POST /actors  
```
(requires authorization header of `post:actors`)
- description: create actor
- required-permission: `post:actors`
- request arguments: 
  - name (required): string
  - age (required): number
  - gender (required): string

- returns status of created actor
```
{
    "success": True,
    "actors": [{ 
      id: 2,
      name: "Bill", 
      age: 35,
      gender: "Male"
    }]
}
```

---

```
PATCH /actors/<id>
```
(requires authorization header of `patch:actors`)
- description: updates actor
- request arguments:
  - name (optional): string
  - age (optional): number
  - gender (optional): string

- returns status of updated actor

```
{
    "success": True,
    "actors": [{ 
      id: 1,
      name: "Bill", 
      age: 25,
      gender: "Male"
    }]
}
```

---

```
DELETE /actors/</id>
```
- description: deletes actor
- required-permission: `delete:actors`
- request arguments: None
- return status of deleted actor
```
{
    "success": True,
    "delete": 2
}
```

---



## author
Denis Tsoi <denistsoi@gmail.com>