from application import app

if __name__ == '__main__':
    debugMode = 'True' #app.config['DEBUG'] == 'True'
    app.run(host='0.0.0.0', debug=debugMode)