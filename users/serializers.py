from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
# from allauth.account.utils import setup_user_email
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer 
from dj_rest_auth.serializers import TokenSerializer
from dj_rest_auth.models import get_token_model
# from .models import AnonUser
from django.core.exceptions import ValidationError as DjangoValidationError

UserModel = get_user_model()
TokenModel = get_token_model()

class UserSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    @staticmethod
    def validate_username(username):
        if "allauth.account" not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
            return username

        # from allauth.account.adapter import get_adapter

        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, "USERNAME_FIELD"):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, "email"):
            extra_fields.append('email')
        if hasattr(UserModel, "first_name"):
            extra_fields.append("first_name")
        if hasattr(UserModel, "last_name"):
            extra_fields.append("last_name")
        
        if(hasattr(UserModel, "role")):
            extra_fields.append("role")
        
        if hasattr(UserModel, "date_joined"):
            extra_fields.append("date_joined")
        model = UserModel
        fields = ("pk", *extra_fields)
        read_only_fields = ("email",)
    
class CustomTokenSerializer(TokenSerializer):
    """
    Serializer for Token model.
    """
    # token = serializers.CharField()
    # user = UserSerializer(read_only=True)
    class Meta:
        model = TokenModel
        fields = ('key','user')
        # depth = 1

class NewUserSerializer(serializers.ModelSerializer):
    """
    Serializer for New User
    """
    class Meta:
        model = UserModel
        fields = ('pk','email')
        read_only_fields = ("email",)