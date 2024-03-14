from flask import Flask, render_template

app = Flask("SuperScrapper")

# @ = decorator finds the function right under itself
# and python knows if someone request to join that route, this function should be done.
@app.route("/")
def home():
  return render_template("potato.html")

##                  Dynamic URLS
# <> mean 'PlaceHolder' and, Python will call 
#fucntion with <PlaceHolder> ex) contact(username)
@app.route("/<username>")
def contact(username):
  return f"hello {username} how are you"

# this host is only for repl.it
app.run(host="0.0.0.0")