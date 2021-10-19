from flask import Flask, request
from threading import Thread
import logging
import sys

app = Flask("")
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@app.route("/")
def home():
    return "Hello. I am alive!"


def github_deploy(request):
    # The repli.<verb> mechanism originates from:
    # https://github.com/khrj/repl.deploy
    # when a request is received, log in the following format:
    # repl.deploy<insert json body here (don't include the angle brackets)>
    # <insert "Signature" header here (don't include the angle brackets)>

    # via stdin the following json format is received:
    # {"status":"403","body":"Invalid Signature"}

    # respond with the given status, and body
    # log to std to stdout: repl.deploy-success
    deploy = "repl.deploy"
    headers = request.headers.get("Signature")
    logging.info(f"{deploy} + {dir(request.json)} + {headers}")

    # response = dict(request.body.get("status"), request.body.get("body"))
    response = response

    return response


# This endpoint exists to support the repl.deploy auto-deployment mechanism.
@app.route("/refresh", methods=["GET", "POST"])
def refresh():
    if request.method == "GET":
        return "I refreshed."

    if request.method == "POST":
        return github_deploy(request)
        logging.info("repl.deploy-success")

    else:
        return f"The {request.method} selected is not supported here."


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
