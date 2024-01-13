"""
URL configuration for anova_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from users.views import GithubLogin, GithubConnect, GoogleLogin, GoogleConnect

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Anova API",
#         default_version="v1",
#         description="Endpoints for the Anova API",
#         contact=openapi.Contact(email="ibk2k7@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
     path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
     path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
     path('dj-rest-auth/github/connect/', GithubConnect.as_view(), name='github_connect'),
     path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
     path('dj-rest-auth/google/connect/', GoogleConnect.as_view(), name='google_connect'),
     path('accounts/', include('allauth.urls')),
    path("bids/", include("bids.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
