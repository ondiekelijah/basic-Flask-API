from api.app import create_app,db
from api.models import User


def deploy():

	"""Run deployment tasks."""

	app = create_app()
	app.app_context().push()

	db.create_all()

	
deploy()