from application import Resource

def func_test(val):
    return "the function param val: " +str(val)

class HelloWorldEndpoint(Resource):
    def get(self):
        func_ret = func_test('the åäö')
        return {'hello': 'GET world!!!', "the_func": func_ret}
    
    def post(self):
        return {'hello': 'POST world!!!'}
    
    def put(self):
        return {'hello': 'PUT world!!!'}