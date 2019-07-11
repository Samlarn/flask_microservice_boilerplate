from application import api, app, jsonify, render_template, request, make_response
from application.rest import msUserResources
from application.rest import helloWorldResources


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'info'


# ----------------------- ADD REST -----------------------
api.add_resource(helloWorldResources.HelloWorldEndpoint, '/hello')
api.add_resource(helloWorldResources.SecretInformation, '/secret')
api.add_resource(msUserResources.UserRegistration, '/register')
api.add_resource(msUserResources.AllUsers, '/msusers')
