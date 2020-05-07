import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie, db_drop_and_create, insert_seed_records

from datetime import date

casting_assistant_auth_header = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViMzQ0ZWU2YjY5YmMwYzEyZmQwZGZiIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTg4ODExNjE4LCJleHAiOjE1ODg4MTg4MTgsImF6cCI6ImVHNUFLSEFZcnZmMWpUb0dnS2JCd1VkbUlkYVZEV2JkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.VJ3AF_PxKkaJBqP6elR1I4t7rjnH7hx9h-j6le41lHcwAKJ5YAjB5Dlap_UyRgUrJ25AHgpSNM47NFCbtWn4i20UnWLMTprutYmpe-b9dGxWdAgAp_U2gSd2_kbUeerWgnPL8hjDhEXSWr4xdHbbZCc8nZgm1f3zKgdltx3NQ0zxCZ09f0fHG33ulSJQJEPNl6mt7_aOgeaqqu0CPjlYXVG0G6rVub2WROa4CiJ9CTAMyiiUuvN5CSIbZnaeuX8yNAdSQ3ASEIdfPcBqQdkhiSpqI0aAgiLU1Yc9Xc8gbDPLkrwea3icRGjYA_CjSJtzZTg3kjf-g-UXyoO4X2oPpg"
}

casting_director_auth_header = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViMzQ1MzI1NGIxNGMwYzEyN2VlMDY5IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTg4ODExNzQ1LCJleHAiOjE1ODg4MTg5NDUsImF6cCI6ImVHNUFLSEFZcnZmMWpUb0dnS2JCd1VkbUlkYVZEV2JkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.vHWywhMlIWiTig8MLJGSF1xw_Bp23WGL5dSAuZDm1WcAlz1-HoLPYnV4sUlQDB7W2MwEUEcsZ-7WzbyekqqmgaPRPa13SFpsg8td4mBYErJhyPOwoLLbA06jmFC1Y3a5dshyaXqBLPosg944Zhg8it-txlc1hueWdY3M-5NCtb7LpAaLiFD6PSf6Xc-KTx8P1KFk4DkNH_WW3eo6ESRldXW6K4Cx8TtlQAKe2pfDM9byCHRvTG3633fQZ06FbUAcNP640sEFQsbuM7BRVMrsnlELjXaerOoD2qF8R0PN91I2k_ckwtvK0Hl6P9xyJ5CiX_b6Kor4FgXdCmv7NgB8mA"
}

executive_producer_auth_header = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViMzQ1NTQ1NGIxNGMwYzEyN2VlMGU3IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTg4ODExODEyLCJleHAiOjE1ODg4MTkwMTIsImF6cCI6ImVHNUFLSEFZcnZmMWpUb0dnS2JCd1VkbUlkYVZEV2JkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.B_KNCaYuJelPzmhc3jn16SIW4-bPTw9JWHy0H9EL_sCAwpvyrmC21dWxAXJqdRz3YdQW9Hv4h9hlX8ZRgeLn94NmNaVkIytyowKd46UlS5Owg8jLTiJKuCaHypvRCuvSO6N5crMxHkJ399muJ4MeSyxn2Sbfm8rZ3LIyPz33tqkSdMTjHDMInt0DfXRKCJzHaqx2L3CeyYC7AOLmAcMMvEQM4clCUEsok5jqFp-P3Du-GQXLZE02U6JrOvOnTlZ3bgYrJTTLBbeY_LTVYzhRCysqiNbA-tSe48GJ2rj28Mg27niwlukz3AvWiuJKtuCVAcvKSuTNqFX5RW653DWLwg"
}


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

    # --
    # get movies
    # --
    def test_get_movies(self):
        response = self.client().get("/movies", headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(len(data["movies"]), 0)

    def test_get_movies_not_authorized(self):
        response = self.client().get("/movies")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    # --
    # create movies
    # --
    def test_create_movie(self):
        new_movie = {
            "title": "Titanic",
            "release_date": date.today()
        }

        response = self.client().post("/movies", json=new_movie,
                                      headers=executive_producer_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_movie_not_authorized(self):
        new_movie = {
            "title": "Titanic",
            "release_date": date.today()
        }

        response = self.client().post("/movies", json=new_movie,
                                      headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    # --
    # update movies
    # --

    def test_update_movie(self):
        update_movie = {"title": "Avatar"}
        response = self.client().patch("/movies/1", json=update_movie,
                                       headers=casting_director_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_movie_unauthorized(self):
        update_movie = {"title": "Avatar"}
        response = self.client().patch("/movies/1", json=update_movie,
                                       headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    # --
    # delete movie
    # --

    def test_delete_movie(self):
        response = self.client().delete("/movies/1", headers=executive_producer_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_movie_unauthorized(self):
        response = self.client().delete("/movies/1", headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    def test_delete_movie_not_found(self):
        response = self.client().delete(
            "/movies/5000", headers=executive_producer_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    # --
    # get actors
    # --

    def test_get_actors(self):
        response = self.client().get("/actors", headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(len(data["actors"]), 1)

    def test_get_actors_not_authorized(self):
        response = self.client().get("/movies")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    # --
    # create actor
    # --
    def test_create_actor(self):
        new_actor = {
            "name": "Steve",
            "age": 20,
            "gender": "Male"
        }
        response = self.client().post("/actors", json=new_actor,
                                      headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_actor_not_authorized(self):
        new_actor = {
            "name": "Steve",
            "age": 20,
            "gender": "Male"
        }
        response = self.client().post("/actors", json=new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["message"], "Authorization header is expected.")
        self.assertFalse(data["success"])

    # --
    # update actor
    # --

    def test_update_actor(self):
        updated_actor = {"name": "Bill"}
        response = self.client().patch("/actors/1", json=updated_actor,
                                       headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_actor_unauthorized(self):
        updated_actor = {"name": "Bill"}
        response = self.client().patch(
            "/actors/1", json=updated_actor, headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    # --
    # delete actor
    # --
    def test_delete_actor(self):
        response = self.client().delete("/actors/1", headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_actor_unauthorized(self):
        response = self.client().delete("/actors/1", headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    def test_delete_actor_not_found(self):
        response = self.client().delete("/actors/5000", headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

        # Make the tests conveniently executable.
        # From app directory, run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()
