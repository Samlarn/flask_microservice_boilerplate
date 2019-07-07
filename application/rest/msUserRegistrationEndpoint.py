from application import Resource, reqparse, create_access_token, create_refresh_token
from application.databaseModels.msUsersModel import MSUsersModel

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