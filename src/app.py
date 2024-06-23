#!/usr/bin/env python3

from flask import Flask, request, render_template
from utils.req_data_analyzer import get_all_posts_metrics
from utils.producer import create_new_username_MQ

app = Flask(__name__)

@app.route("/")
def main():
    return '''
        <h1>Dolphin Instagram Metrics</h1>
        <form action="/ig_metrics" method="POST">
            <button name="foo">See IG users data</button>
        </form>
        <form action="/add_ig_username" method="POST">
            <input name="ig_username">
            <input type="submit" value="Add new IG username">
        </form>
     '''

@app.route("/ig_metrics", methods=["POST"])
def ig_metrics():
    # user_input = request.form.get("user_input", "")

    user_input = "Danny" # Hardcoding name, name will be retrieved once adding auth0
    headings = (
        "User ID",
        "Username",
        "Full name", 
        "Posts",
        "Average likes in the last 9 posts",
        "Most recent post date",
        "Last updated")
    data = get_all_posts_metrics()
    return render_template("ig_metrics.html", headings=headings, data=data, user_input=user_input)

@app.route("/add_ig_username", methods=["POST"])
def add_ig_username():
    new_ig_username = request.form.get("ig_username", "")
    create_new_username_MQ(new_ig_username)
    return render_template("new_ig_username.html", ig_username=new_ig_username)

if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=3000, debug=True)