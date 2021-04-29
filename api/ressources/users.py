


from flask import Response, request
 from models import user
from flask_restful import Resource

class UsersApi(Resource):
  def get(self):
    Users = user.objects().to_json()
    return Response(user, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    user = users(**body).save()
    id = user.id
    return {'id': str(id)}, 200
 
class UsersApi(Resource):
  def put(self, id):
    body = request.get_json()
    user.objects.get(id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    user = user.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    user = Users.objects.get(id=id).to_json()
    return Response(user, mimetype="application/json", status=200)