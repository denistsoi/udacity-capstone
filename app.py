import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app)

    # set headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route("/", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy"
        })

    # ---
    # movies
    # ---

    @app.route("/movies", methods=["GET"])
    @requires_auth("get:movies")
    def get_movies(payload):
        movies = Movie.query.all()
        if movies is None:
            abort(404)

        return jsonify({
            "success": True,
            "movies": [movie.format() for movie in movies]
        })

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def create_movie(payload):
        body = request.get_json()

        if "title" and "release_date" not in body:
            abort(422)

        title = body["title"]
        release_date = body["release_date"]

        movie = Movie(title=title, release_date=release_date)
        movie.insert()

        return jsonify({
            "success": True,
            "movies": [movie.format()]
        })

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def update_movies(payload, movie_id):
        body = request.get_json()

        try:
            movie = Movie.query.get(movie_id)

            if movie is None or body is None:
                abort(404)

            else:
                if "title" in body:
                    movie.title = body["title"]
                if "release_date" in body:
                    movie.release_date = body["release_date"]

                movie.update()

                updated_movie = Movie.query.get(movie_id)
                return jsonify({
                    "success": True,
                    "movies": [updated_movie.format()]
                })

        except Exception as error:
            if error.code == 404:
                abort(404)

            abort(422)

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)

            return jsonify({
                "success": True,
                "delete": movie_id
            })
        except Exception as error:
            if (error.code == 404):
                abort(404)

            abort(422)

    # ---
    # actors
    # ---

    @app.route("/actors", methods=["GET"])
    @requires_auth("get:actors")
    def get_actors(payload):
        actors = Actor.query.all()
        if actors is None:
            abort(404)

        return jsonify({
            "success": True,
            "actors": [actor.format() for actor in actors]
        })

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def create_actor(payload):
        body = request.get_json()

        if "name" and "age" and "gender" not in body:
            abort(422)

        name = body["name"]
        age = body["age"]
        gender = body["gender"]

        actor = Actor(name=name, age=age, gender=gender)
        actor.insert()

        return jsonify({
            "success": True,
            "actors": [actor.format()]
        })

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def update_actor(payload, actor_id):
        body = request.get_json()

        try:
            actor = Actor.query.get(actor_id)

            if actor is None or body is None:
                abort(404)

            else:
                if "name" in body:
                    actor.name = body["name"]
                if "age" in body:
                    actor.age = body["age"]
                if "gender" in body:
                    actor.gender = body["gender"]

                actor.update()
                updated_actor = Actor.query.get(actor_id)
                return jsonify({
                    "success": True,
                    "actors": [updated_actor.format()]
                })

        except Exception as error:
            abort(422)

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if actor is None:
                abort(404)

            return jsonify({
                "success": True,
                "delete": actor_id
            })
        except Exception as error:
            if (error.code == 404):
                abort(404)

            abort(422)

    # error handlers
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized Error"
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(AuthError)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error["description"]
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
