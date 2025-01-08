from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from django.db import transaction

class CreateAccountView(APIView):
    def post(self, request):
        
        # Start a transaction to ensure atomicity
        with transaction.atomic():
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                # Create the account
                account = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GetAccountView(APIView):
    def get(self, request, account_id):
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(account)
        return Response(serializer.data)