from application import Resource
from application.databaseModels.msUsersModel import MSUsersModel

class AllUsers(Resource):
    def get(self):
        return MSUsersModel.return_all()
  
