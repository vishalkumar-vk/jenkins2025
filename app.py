from flask import Flask

app = flask(__name__)

@app.route("/info")
def fun():
    return "Welcome to my progrgram...."
app.run(host='0.0.0.0')
