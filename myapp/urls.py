from django.urls import path
from .views import CreateAccountView,GetAccountView,Transaction

urlpatterns = [
    path('', CreateAccountView.as_view(), name='create_account'),
    path('<int:account_id>/', GetAccountView.as_view(), name='get_account'),
    path('transfers/', Transaction.as_view(), name='transaction'),
    
]
