import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie, db_drop_and_create, insert_seed_records


class AgencyTestCase(unittest.TestCase):
    """Agency test case"""

    def setUp(self):
        """define test variables and init app"""

        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', "agency_test")

        setup_db(self.app, self.database_path)
        db_drop_and_create()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def test_get_movies(self):
        response = self.client().get("/movies")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["movies"]), 0)

    def test_get_actors(self):
        response = self.client().get("/actors")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["actors"]), 1)


# Make the tests conveniently executable.
# From app directory, run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()
