from flask import Blueprint, render_template

error = Blueprint("error_bp", __name__)


@error.app_errorhandler(400)
def bad_request(e):
    return render_template("errors/401.html", title="Bad Request"), 400


@error.app_errorhandler(401)
def unauthorized(e):
    return render_template("errors/401.html", title="Unauthorized"), 401


@error.app_errorhandler(403)
def forbidden(e):
    return render_template("errors/401.html", title="Access Forbidden"), 403


@error.app_errorhandler(405)
def method_not_allowed(e):
    return render_template("errors/401.html", title="Method Not Allowed"), 405


@error.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html", title="Not Found"), 404


@error.app_errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html", title="Server Error"), 500


@error.app_errorhandler(503)
def service_unavailable(e):
    return render_template("errors/503.html", title="Service Unavailable"), 503
