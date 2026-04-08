from django.db import models

class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField()

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
        else:
            print('Amount is not applicable')
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.save
        else:
            print("Insufficient Balance")