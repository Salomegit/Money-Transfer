from django.utils.timezone import now
from django.db import models

class Account(models.Model):
    account_no = models.CharField(max_length=20, unique=True)
    balance = models.FloatField()

    def __str__(self):
        return f"Account {self.account_no}"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.save()


class Transaction(models.Model):
    source_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="outgoing_transactions", null=True, blank=True)
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="incoming_transactions")
    amount = models.FloatField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Transaction of {self.amount} from {self.source_account} to {self.destination_account}"
