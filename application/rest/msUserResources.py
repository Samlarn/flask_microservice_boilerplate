from application.database.models import MSUsersModel
from application import create_access_token
from application import create_refresh_token
from application import jwt_refresh_token_required
from application import get_jwt_identity
from application import Resource
from application import reqparse


parser = reqparse.RequestParser()
parser.add_argument('msname', help = 'This field cannot be blank!', required = True)
parser.add_argument('password', help = 'This field cannot be blank!', required = True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        print(data)
        if MSUsersModel.find_by_username(data['msname']):
            return {'message': 'User {} already exists'.format(data['msname'])}
        
        new_user = MSUsersModel(
            msname = data['msname'],
            password = MSUsersModel.generate_hash(data['password'])
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['msname'])
            refresh_token = create_refresh_token(identity = data['msname'])
            return {
                'message': 'User {} was created'.format(data['msname']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500



class MSUserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = MSUsersModel.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if MSUsersModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_msuser = get_jwt_identity()
        access_token = create_access_token(identity = current_msuser)
        return {'access_token': access_token}



class AllUsers(Resource):
    def get(self):
        return MSUsersModel.return_all()