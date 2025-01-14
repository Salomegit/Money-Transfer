from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer, TransactionSerializer
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
            account = Account.objects.select_for_update().get(id=account_id)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
class Transaction(APIView):   
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        # Validate input data
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        source_account_id = serializer.validated_data.get('source_account').id if serializer.validated_data.get('source_account') else None
        destination_account_id = serializer.validated_data['destination_account'].id
        amount = serializer.validated_data['amount']

        try:
            with transaction.atomic():
                source_account = None
                if source_account_id:
                    source_account = (
                        Account.objects.select_for_update().get(id=source_account_id)
                    )
                
                destination_account = (
                    Account.objects.select_for_update().get(id=destination_account_id)
                )

                # Perform balance updates
                if source_account:
                    if source_account.balance < amount:
                        return Response(
                            {"error": f"Source account {source_account.account_no} has insufficient funds."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    source_account.withdraw(amount)

                destination_account.deposit(amount)

                # Save the transaction
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Account.DoesNotExist:
            return Response({"error": "One or both accounts do not exist."}, status=status.HTTP_404_NOT_FOUND)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "An error occurred during the transaction."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)