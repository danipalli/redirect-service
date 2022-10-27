import flask

app = flask.Flask(__name__)


@app.get("/")
def redirect():
    args = flask.request.args
    redirect_url = args.get("redirect", "error", type=str)
    redirect_code = args.get("status", 303, type=int)

    if redirect_url is None:
        return 400

    response = flask.Response("Test")
    response.headers["Location"] = redirect_url
    response.status = redirect_code
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=False)
