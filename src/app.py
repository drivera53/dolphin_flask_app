#!/usr/bin/env python3

from flask import Flask, request, render_template
from utils.req_data_analyzer import get_all_posts_metrics

app = Flask(__name__)

@app.route("/")
def main():
    return '''
        <h1>Dolphin Instagram Metrics</h1>
        <form action="/ig_metrics" method="post">
            <button name="foo">See IG users data</button>
        </form>
        <form action="/ig_metrics" method="POST">
            <input name="user_input">
            <input type="submit" value="Add new IG username">
        </form>
     '''

headings = (
    "User ID",
    "Username",
    "Full name", 
    "Posts",
    "Average likes in the last 9 posts",
    "Most recent post date",
    "Last updated")
# data = (
#     ("samboard", "Yes", "No", "796", "209", "Jan 11, 2022", "4627", "5059", "May 18, 2024"),
#     ("sk8mafia", "Yes", "Yes", "7641", "1033", "May 17, 2024", "429K", "1570", "May 17, 2024 "),
#     (".....", ".....", ".....", ".....", ".....", ".....", ".....", ".....", ".....")
# )
@app.route("/ig_metrics", methods=["POST"])
def ig_metrics():
    # user_input = request.form.get("user_input", "")
    user_input = "Danny" # Hardcoding name, name will be retrieved once adding auth0
    data = get_all_posts_metrics()
    return render_template("ig_metrics.html", headings=headings, data=data, user_input=user_input)

if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=3000, debug=True)