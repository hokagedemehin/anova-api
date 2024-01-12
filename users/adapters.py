from allauth.account.adapter import DefaultAccountAdapter
import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user =  super().save_user(request, user, form, commit)
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.role = form.cleaned_data.get('role')
        
        user.save()
        return user
    
    def get_email_confirmation_url(self, request, emailconfirmation):
        FRONTEND_URL = env('FRONTEND_URL')
        return "{}/confirm-email?token={}".format(FRONTEND_URL,emailconfirmation.key)