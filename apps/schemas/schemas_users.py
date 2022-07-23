from database.database import ma
from apps.models.user_models import UsersModel
class UserSchema(ma.Schema):
    class Meta:
        model= UsersModel
        fields = ('id','email','name')