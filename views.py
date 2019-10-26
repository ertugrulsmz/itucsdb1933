from flask import render_template


def home_page():
    return render_template("home.html", name="home_page")


def blog_page():
    return render_template("blog.html", name="blog_page")


def profile_page():
    return render_template("profile.html", name="profile_page")