from application import app, jwt
from application.database.models import RevokedTokenModel


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


if __name__ == '__main__':
    debugMode = 'True' #app.config['DEBUG'] == 'True'
    app.run(host='0.0.0.0', debug=debugMode)