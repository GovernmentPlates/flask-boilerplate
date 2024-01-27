from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import auth
from app.models import Users
from app import db

from app.modules.util.decorators import redirect_if_already_authenticated
from app.modules.util.auth import (
    check_if_user_already_exists,
    check_password_confirmation,
    check_password_strength,
)
from app.modules.util.forms import collect_form_data


@auth.route("/login", methods=["GET", "POST"])
@redirect_if_already_authenticated
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Your credentials are invalid", "warning")
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("main.index"))

    return render_template("auth/login.html", title="Sign In", form=form)


@auth.route("/register", methods=["GET", "POST"])
@redirect_if_already_authenticated
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        old_form_data = collect_form_data(
            form.first_name, form.last_name, form.email
        )

        if check_if_user_already_exists(form.email.data):
            flash("Email invalid or already in use", "warning")
            return render_template(
                "auth/register.html",
                title="Register",
                form=form,
                old_form_data=old_form_data,
            )

        if not check_password_confirmation(
            form.password.data, form.repeat_password.data
        ):
            flash("Passwords do not match", "warning")
            return render_template(
                "auth/register.html",
                title="Register",
                form=form,
                old_form_data=old_form_data,
            )

        if not check_password_strength(form.password.data):
            flash("Password is not strong enough", "warning")
            return render_template(
                "auth/register.html",
                title="Register",
                form=form,
                old_form_data=old_form_data,
            )

        user = Users(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Account successfully registered", "success")
        return redirect(url_for("auth.login"))

    return render_template(
        "auth/register.html", title="Register", form=form, old_form_data=None
    )


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You've signed out", "success")
    return redirect(url_for("auth.login"))
