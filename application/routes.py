from application import api, app, jsonify, render_template, request, make_response
from application.rest import helloWorldRest
from application.rest.msUserRegistrationEndpoint import UserRegistration


@app.route('/')
def index():
    return render_template('index.html')


# ----------------------- ADD REST -----------------------
api.add_resource(helloWorldRest, '/hello')
api.add_resource(UserRegistration, '/registration')
