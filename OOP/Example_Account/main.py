from libraries.Account import Account
from decimal import Decimal


account1 = Account("Cristiano M.", Decimal("200.00"))
account1.deposit(Decimal("100.00"))
account1.withdraw(Decimal("50.00"))

account1.balance = Decimal("50.00")


