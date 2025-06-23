from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/clothing")
def clothing():
    return render_template("clothing.html")

@app.route("/shoes")
def shoes():
    return render_template("shoes.html")

if __name__ == "__main__":
    app.run(debug=True)