from django.urls import path
from . import views
from rest_framework import routers
from anova_backend.router import CustomRouter

custom_router = CustomRouter()
simple_router = routers.SimpleRouter()

simple_router.register(r'history', views.BidsHistoryViewSets, basename='bids_history')
simple_router.register(r'admin', views.AdminBidsViewSets, basename='bids_history')
custom_router.register(r'', views.BidsViewSets, basename='bids')

urlpatterns = [
    path('list/', views.bids_list, name='bids_list'),
    path('history/list/<int:id>/', views.bids_history, name='bids_history'),
    path('admin/history/list/<int:id>/', views.admin_bids_history, name='admin_bids_history_list'),
]

urlpatterns += simple_router.urls
urlpatterns += custom_router.urls
