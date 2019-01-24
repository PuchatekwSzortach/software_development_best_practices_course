"""
Module with server requests acceptance tests
"""

import application


def test_factorial_endpoint_with_simple_input():

    app = application.get_app()
    assert app is not None

    with app.test_client() as client:

        response = client.get("/factorial?input=3")

        assert response.status_code == 200

        expected = "3! = 6"
        assert expected in response.get_data(as_text=True)
