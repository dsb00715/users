from project import create_app
from flask import jsonify

app = create_app()


@app.route("/users/ping", methods=["GET"])
def ping_pong():
    return jsonify({"status": "success", "message": "pong!"})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
