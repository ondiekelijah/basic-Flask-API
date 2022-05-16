import json
from unicodedata import name
from urllib import response
from api.models import User


def test_new_user(client, init_database):
    """
    GIVEN the User model
    WHEN a new user is created
    THEN check that the name & email fields are defined correctly
    """
    user = User(name='Cheryl', email="kiddo@gmail.com", password="12345")
    assert user.name == 'Cheryl'
    assert user.email == 'kiddo@gmail.com'


def test_fetch_user(client, init_database):

    path = "api/v1/1"
    response = client.get(path)
    assert b'{"email":"test1@gmail.com","id":1,"name":"Test User 1"}\n' in response.data


def test_fetch_users(client, init_database):

    path = "api/v1/users"
    response = client.get(path)
    assert b'[{"email":"test1@gmail.com","id":1,"name":"Test User 1"},{"email":"test2@gmail.com","id":2,"name":"Test User 2"},{"email":"test3@gmail.com","id":3,"name":"Test User 3"}]\n' in response.data


def test_update_user(client, init_database):
    path ="api/v1/1/update"
    response =client.post(path,
     json ={
         "id":1,
         "name":"hunter",
         "email":"hunterfields@gmail.com",
     },
    )
    assert b'{"email":"hunterfields@gmail.com","id":1,"name":"hunter"}\n' in response.data

def test_delete_user(client, init_database):
    path= "api/v1/1/delete"
    response= client.post(path)
    assert response.status_code == 200
    assert b'User has been deleted' in response.data