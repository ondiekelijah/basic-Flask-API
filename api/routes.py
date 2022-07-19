from api.app import create_app, db
from api.models import User,user_schema, users_schema
from flask import request,redirect,jsonify

app = create_app()

# Home endpoint
@app.get('/')
def home():
    return 'Welcome to the API'
    

@app.post("/api/v1/users/add")
def create():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    try:
       user = User(name=name,email=email,password=password)
       db.session.add(user)
       db.session.commit()
       
       created_user = User.query.filter_by(email=email).first()

    except Exception as e:
        print(f"Error {e}")
    
    return user_schema.dump(created_user)

@app.get("/api/v1/users/<int:id>")
def get_user(id):
    user = User.query.filter_by(id=id).first()
    return user_schema.dump(user) 

@app.get("/api/v1/users")
def get_users():
    users = User.query.all()
    all_users = users_schema.dump(users) 
    return jsonify(all_users)


@app.put("/api/v1/users/<int:id>/update")
def update(id):
    user=User.query.filter_by(id=id).first()

    if user:
        name = request.json["name"]
        email = request.json["email"]

        user.name = name
        user.email = email

        db.session.commit()

    return user_schema.dump(user) 

@app.delete("/api/v1/users/<int:id>/delete")
def delete(id):
    user=User.query.filter_by(id=id).first()
    if request.method == "POST":
        if user:
           db.session.delete(user)
           db.session.commit()

    return jsonify("User has been deleted")
