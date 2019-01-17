import flask

import utilities


def get_app():
    """
    Create web app
    :return: Returns web application server object
    """

    app = flask.Flask("software_development_best_practices_course")

    @app.route("/factorial")
    def get_factorial_endpoint():

        if "input" in flask.request.args:

            input = int(flask.request.args["input"])
            output = utilities.get_factorial(input)

            return flask.render_template("factorial.html", input=input, output=output)

        return "provide input please!"

    return app


def main():

    app = get_app()
    app.run(host="0.0.0.0", port=5001)


if __name__ == "__main__":

    main()
