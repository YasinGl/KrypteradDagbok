from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Välkommen till din personliga dagbok och journalapplikation!"

if __name__ == '__main__':
    app.run(debug=True)

