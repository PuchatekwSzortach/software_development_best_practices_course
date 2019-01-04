import flask


APP = flask.Flask("software_development_best_practices_course")


@APP.route("/factorial")
def get_factorial():

    return "1"


def main():

    APP.run(host="0.0.0.0")


if __name__ == "__main__":

    main()
