from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def run(host: str = "0.0.0.0", 
        port: int = 2026, 
        debug: bool = True
    ) -> None:
    
    app.run(host=host, port=port, debug=debug)