from rest_framework import serializers
from .models import Account, Account_Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_no', 'balance']
 
    def validate_balance(self, value):
        # Balance should always be greater than 0 when creating an account.
        if value <= 0:
            raise serializers.ValidationError("The starting balance must be greater than zero.")
        return value


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Transaction
        fields = ['id', 'source_account', 'destination_account', 'amount', 'timestamp']

    def validate(self, data):
       
        source_account = data.get('source_account')
        destination_account = data.get('destination_account')
        amount = data.get('amount')

        if amount <= 0:
            raise serializers.ValidationError("Transfer amount must be greater than zero.")
        
        #Validation for Insufficient funds from the source Account
        
        if source_account and source_account.balance < amount:
            raise serializers.ValidationError(f"Source account {source_account.account_no} has insufficient funds.")
        
        # validation for source and destination account being same
        if source_account and source_account == destination_account:
            raise serializers.ValidationError("Source and destination accounts must be different.")

        return data

    def create(self, validated_data):
       
        source_account = validated_data.get('source_account')
        destination_account = validated_data['destination_account']
        amount = validated_data['amount']

        # Handle source account balance if provided
        if source_account:
            source_account.withdraw(amount)

        # Add the amount to the destination account
        destination_account.deposit(amount)

        # Create and return the transaction
        return super().create(validated_data)
