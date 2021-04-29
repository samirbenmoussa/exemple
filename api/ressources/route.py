from .users import UsersApi, UsersApi

def initialize_routes(api):
 api.add_resource(UsersApi, '/api/user')
 api.add_resource(UsersApi, '/api/user/<id>')