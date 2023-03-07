"""Main module for Hubspot APIs """

from flask import Flask, request
from flask_cors import cross_origin

from app.main_handler import generate_tokens, create_auth_url

app = Flask(__name__)

#################################################################################################

@app.route(rule="/url/", methods=["GET", ])
@cross_origin()
def auth_url():
    """generate auth URL """
    return create_auth_url()

@app.route(rule="/tokens/", methods=["GET", ])
@cross_origin()
def credentials():
    """exchange authorization code for tokens """
    return generate_tokens(request)

#################################################################################################

if __name__ == "__main__":
    app.run()

