import os
from pathlib import Path
import environ
from django.contrib.sites.shortcuts import get_current_site
from dj_rest_auth.forms import AllAuthPasswordResetForm
from allauth.account.forms import default_token_generator
from allauth.account.utils import (
    user_pk_to_url_str,
)
from allauth.utils import build_absolute_uri
from allauth.account.adapter import get_adapter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
FRONTEND_URL = env('FRONTEND_URL')

class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)
        for user in self.users:
            temp_key = token_generator.make_token(user)
            
            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            # path = reverse(
            #     'password_reset_confirm',
            #     args=[user_pk_to_url_str(user), temp_key],
            # )
            path = f"{FRONTEND_URL}/reset-password/{user_pk_to_url_str(user)}/{temp_key}"
            # if api_settings.PASSWORD_RESET_USE_SITES_DOMAIN:
            #     url = build_absolute_uri(None, path)
            # else:
            url = build_absolute_uri(request, path)
            url = url.replace("%3F", "?")
            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
            }
            get_adapter().send_mail(
                'account/email/password_reset_key',
                email,
                context,
            )
            return user