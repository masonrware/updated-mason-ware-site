#!usr/bin/python

# app.py
# Version 1.0.0
# 2/27/22

import argparse

from flask import Flask, render_template, request

app = Flask(__name__)

##this is an update to test deploy

class BackEndApplication:
    """Class for the base back end app of the site in Flask"""
    @app.route('/')
    def landing_page():
        """root landing page"""
        return render_template('index.html')

    @app.route("/home/")
    def home():
        """home page"""
        return render_template("index.html")

    @app.route('/about/')
    def about():
        """about page"""
        return render_template("about.html")

    @app.route('/portfolio/')
    def portfolio():
        """portfolio page"""
        return render_template("portfolio.html")

    @app.route('/resources/')
    def resources():
        """resources page"""
        return render_template("resources.html")

    @app.route('/resume/')
    def resume():
        """resume page"""
        return render_template("resume.html")

    @app.route('/update_server/', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('path/to/git_repo')
            origin = repo.remotes.origin
            origin.pull()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Boolean IR system")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--run", action="store_true")

    args = parser.parse_args()

    if args.build:
        print('building site necessitites....')
    if args.debug:
        app.run(debug=True, port=5000)
    if args.run:
        app.run(debug=False, port=5000)
