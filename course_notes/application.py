"""
Module creating flask application
"""

import flask


def get_app():

    app = flask.Flask("software_development_best_practices_course")

    @app.route("/software_development_best_practices_course")
    def render_index():
        return flask.render_template("index.html")

    return app
