from django.urls import path
from authentication.views import TokenGenerateView, TokenValidateView

urlpatterns = [
    path('generate/', TokenGenerateView.as_view(), name='token-generate'),
    path('validate/', TokenValidateView.as_view(), name='token-validate'),
]
