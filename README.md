# Fyle Backend Challenge
Hello everyone at Fyle, 

I really love the the new format of the assignment, the requirements were clearly stated, even though I had little to no prior experience with Flask, as I had worked extensively with Django and FastAPI, the repo was easy to work on.

- [x] Added Missing Missing APIs - [Postman Documentation](https://documenter.getpostman.com/view/21779136/2s9YsNdqVj)

![Tests with Coverage](images/tests-coverage.png)
- [x] Automated Tests are Working 
- [x] Improved the Test Coverage to 95% and added some additional tests for grading API

![Dockersised the application](images/docker.png)
- [x] Dockerised the Application with Dockerfile and docker-compose.yml

Here are the following things I noticed about repo and could be improved:

### Problem 1
Problem: There is no check in the header to check if the id for principal, teacher or student exists in the database or not.

Solution: Query the database whether it exists or not

### Problem 2
Problem: Exposing sequential id in the headers is big security threat and can be easily guessed by the user

Solution:
- Apply Rate-Limiting to the APIs
- Keep auto_increment ids as primary key, implement uuid to implement a external_id, this will be used to reference the objects in the APIs

### Problem 3
Problem: No separate test database, tests directly run on production server.

Solution: Create a separate test database, create fake data and delete the database after tests are run.

### Problem 4
Problem: Ids hard encoded in database

Solution: Make use of pytest fixtures or query from database for ids that fullfill a certain condition like get assignments with state "GRADED" and etc.

## Installation

### Run using Docker
To run the docker on local machine simply run the following command:
```
docker-compose up -d
```

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
