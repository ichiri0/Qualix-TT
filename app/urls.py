from django.urls import path
from .views import RpcCallView

urlpatterns = [
    path('rpc_call', RpcCallView.as_view(), name='rpc_call'),
]