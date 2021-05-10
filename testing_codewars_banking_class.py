from codewars_kata_banking_class import *

Clem, john = User('ClEm',150,True), User('joHn',100, False)

#print(Clem.__dict__)
# print(Clem.__doc__)
# print(Clem.__module__)
# print(john.name) # should be capitalized
# print(Clem.name) # should be capitalized
# print(Clem.add_cash(33))
# Clem.check(john,10)
# print(Clem.withdraw(26))

god = Superuser('gOd', 10**100, True, isgreat='yes')
print(god.__dict__)
print(god.power)