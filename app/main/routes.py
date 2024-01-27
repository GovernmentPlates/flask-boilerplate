from flask import render_template, __version__
from app.main import main
from os import environ

# Versions of Python, Flask as well as other packages (displayed on the index)
# This can be removed if you don't want to display this information
from platform import python_version
from pip import __version__ as pip_version
from flask_login import __version__ as flask_login_version
from flask_sqlalchemy import __version__ as flask_sqlalchemy_version
from sqlalchemy import __version__ as sqlalchemy_version
from jinja2 import __version__ as jinja2_version
from dotenv import version as dotenv_version
from flask_wtf import __version__ as flask_wtf_version
from wtforms import __version__ as wtforms_version


@main.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        flask_version=__version__,
        python_version=python_version(),
        pip_version=pip_version,
        jinja2_version=jinja2_version,
        flask_login_version=flask_login_version,
        flask_sqlalchemy_version=flask_sqlalchemy_version,
        sqlalchemy_version=sqlalchemy_version,
        flask_wtf_version=flask_wtf_version,
        wtforms_version=wtforms_version,
        dotenv_version=dotenv_version.__version__,
        debug_enabled=environ.get("FLASK_DEBUG"),
    )


@main.route("/main", methods=["GET"])
def main():
    return render_template("main/index.html")
