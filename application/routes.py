from application import api, app, jsonify, render_template, request, make_response
from application.rest import helloWorldEndpoint, msUserRegistrationEndpoint, msUsersEndpoint


@app.route('/')
def index():
    return render_template('index.html')


# ----------------------- ADD REST -----------------------
api.add_resource(helloWorldEndpoint.HelloWorldEndpoint, '/hello')
api.add_resource(msUserRegistrationEndpoint.UserRegistration, '/register')
api.add_resource(msUsersEndpoint.AllUsers, '/msusers')
