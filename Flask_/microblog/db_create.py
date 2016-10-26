#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

#this script is completely generic - use for any application
# how to execute:
# $ chmod a+x script.py
#$ ./script.py <arguments> - will create app.db file + db_repository folder with files in it.
#Here SQLAlchemy-migrate stores its data files. Note that we do not regenerate the repository if it already exists.
# This will allow us to recreate the database while leaving the existing repository if we need to.
