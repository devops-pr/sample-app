# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the world of KUBER!"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")