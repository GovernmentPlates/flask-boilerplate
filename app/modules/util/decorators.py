from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def redirect_if_already_authenticated(f):
    """
    Redirects to the index page if the user is already authenticated.

    :return: redirect to `main.index`
    """

    @wraps(f)
    def is_authenticated(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)

    return is_authenticated
