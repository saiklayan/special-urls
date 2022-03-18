from app2.views import app2_RRR
from django.urls import path
app_name='app2'
urlpatterns=[
    path('app2_RRR/',app2_RRR,name='app2_RRR')
]