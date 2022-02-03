from flask import (
    Flask,
    render_template,
    Blueprint
)

# Create an application instance
app=Blueprint("root",__name__)

@app.post("/", strict_slashes=False)
def create_post():
    return {"message": "post created "}


@app.get("/", strict_slashes=False)
def get_posts():
    return {"message": "all posts"}


@app.put("/", strict_slashes=False)
def update_post():
    return {"message": "post updated"}


@app.delete("/", strict_slashes=False)
def delete_post():
    return {"message": "post deleted"}

