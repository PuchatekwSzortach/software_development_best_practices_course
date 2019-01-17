import flask

import utilities

APP = flask.Flask("software_development_best_practices_course")


@APP.route("/factorial")
def get_factorial_endpoint():

    if "input" in flask.request.args:

        input = int(flask.request.args["input"])
        output = utilities.get_factorial(input)

        return flask.render_template("factorial.html", input=input, output=output)

    return "provide input please!"


def main():

    APP.run(host="0.0.0.0", port=5001)


if __name__ == "__main__":

    main()
