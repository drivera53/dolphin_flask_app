#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return '''
        <h1>Enter your Instagram Username</h1>
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

headings = (
    "Username", 
    "Follower", 
    "Following",
    "Posts",
    "Average likes in the last 9 posts",
    "Most recent post date",
    "Number of followers",
    "Number of followings",
    "Last updated")
data = (
    ("samboard", "Yes", "No", "796", "209", "Jan 11, 2022", "4627", "5059", "May 18, 2024"),
    ("sk8mafia", "Yes", "Yes", "7641", "1033", "May 17, 2024", "429K", "1570", "May 17, 2024 "),
    (".....", ".....", ".....", ".....", ".....", ".....", ".....", ".....", ".....")
)
@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    user_input = request.form.get("user_input", "")
    return render_template("table.html", headings=headings, data=data, user_input=user_input)