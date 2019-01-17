"""
Module with utilities
"""


def get_factorial(x):
    """
    Computes factorial of x
    :param x: int
    :return: int
    """

    if x < 0:
        raise ValueError("Input must be positive, but {} was given")

    factorial = 1

    for value in range(1, x + 1):

        factorial *= value

    return factorial


def get_eyes(image):
    """
    Gets bounding box coordinates of all eyes in input image
    :param image: image
    :return: list of bounding boxes coordinates, one box for each eye found in input image
    """

    # spoof implementation
    return []


def get_mouths(image):
    """
    Gets bounding box coordinates of all mouths in input image
    :param image: image
    :return: list of bounding boxes coordinates, one box for each mouth found in input image
    """

    # spoof implementation
    return []


def get_faces(image):
    """
    Gets bounding box coordinates of all faces in input image
    :param image: image
    :return: list of bounding boxes coordinates, one box for each face found in input image
    """

    # Get eyes and mouths in the image
    eyes = get_eyes(image)
    mouths = get_mouths(image)

    # Sort through eyes and mouths to figure out which combinations can make valid faces
    # ....

    # spoof implementation
    faces = []

    return faces
