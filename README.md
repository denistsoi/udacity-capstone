# capstone project

## description

Udacity Fullstack capstone project

## criteria

### General Specifications

- [ ] Models will include at least…
  - [ ] Two classes with primary keys at at least two attributes each
  - [ ] [Optional but encouraged] One-to-many or many-to-many relationships between classes

- [ ] Endpoints will include at least…
  - [ ] Two GET requests
  - [ ] One POST request
  - [ ] One PATCH request
  - [ ] One DELETE request

- [ ] Roles will include at least…
  - [ ] Two roles with different permissions
  - [ ] Permissions specified for all endpoints

- [ ] Tests will include at least….
  - [ ] One test for success behavior of each endpoint
  - [ ] One test for error behavior of each endpoint
  - [ ] At least two tests of RBAC for each role


Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:

- [x] Movies with attributes title and release date
- [x] Actors with attributes name, age and gender

Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database

Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role

<!-- https://dev-98w9-5eh.auth0.com/authorize?audience=agency&response_type=token&client_id=eG5AKHAYrvf1jToGgKbBwUdmIdaVDWbd&redirect_uri=http://localhost:5000 -->

casting_assistant@example.com #m5V@ccgFMO7
casting_director@example.com 7a03jR%F6R1d
executive_producer@example.com 1CU1OJppfe0$



## author
Denis Tsoi <denistsoi@gmail.com>