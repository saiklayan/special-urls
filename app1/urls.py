from app1.views import app1_NWH
from django.urls import path
app_name='app1'
urlpatterns=[
    path('app1_NWH/',app1_NWH,name='app1_NWH')
]