from api.app import create_app, db
from api.models import User,user_schema, users_schema
from flask import request,redirect,jsonify

app = create_app()

@app.route("/api/v1/add", methods=['GET','POST'])
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

@app.route("/api/v1/<int:id>",methods=['GET','POST'])
def RetrieveSingleUser(id):
    user = User.query.filter_by(id=id).first()
    return user_schema.dump(user) 

@app.route("/api/v1/users", methods=['GET','POST'])
def RetrieveSingleUsers():
    users = User.query.all()
    all_users = users_schema.dump(users) 
    return jsonify(all_users)


@app.route("/api/v1/<int:id>/update", methods=['GET','POST'])
def update(id):
    user=User.query.filter_by(id=id).first()

    if user:
        name = request.json["name"]
        email = request.json["email"]
        # password = request.json["password"]
        user.name = name
        user.email = email

        db.session.commit()

    return user_schema.dump(user) 

@app.route("/api/v1/<int:id>/delete", methods=['GET','POST'])
def delete(id):
    user=User.query.filter_by(id=id).first()
    if request.method == "POST":
        if user:
           db.session.delete(user)
           db.session.commit()

    return jsonify("User has been deleted")


# if __name__ == "__main__":
#     app.run(debug=True)