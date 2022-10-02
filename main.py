# a = amount
# b = balance
# class Bank_Account:
#     def __init__(self):
#         self.b = 0
#     def deposit(self):
#         a = float(input("Enter the amount you want to pay: "))
#         self.b = self.b + a
#         print("Amount deposited:", a)
#     def withdraw(self):
#         a = float(input("Enter the amount you want take off: "))
#         if self.b >= a:
#             self.b = self.b - a
#             print("Amount to withdraw:", a)
#         else:
#             print("Not enough balance ")
#     def balance(self):
#         print("Available balance: ", self.b)
# ba = Bank_Account()
# ba.deposit()
# ba.withdraw()
# ba.balance()

# class Money_converter:
#     def __init__(self):
#         self.b = 0
#     def money(self):
#         a = float(input("Enter the amount of TG you want to pay: "))
#         self.b = self.b + a
#         print("Amount deposited: ", a)
#     def convert(self):
#         t = float(input("Enter the amount of tenge you want to convert: "))
#         c = float(input("Choose wallet type \n 1. USD \n 2. Euro \n 3. Rub \n 4. Yuan \n"))
#         if c == 1:
#             u = 480
#             n = t / u
#             print("Available ", n, " dollars")
#         elif c == 2:
#             e = 469
#             n = t / e
#             print("Available ", n, " euro")
#         elif c == 3:
#             r = 7.45
#             n = t / r
#             print("Available ", n, " rubles")
#         elif c == 4:
#             y = 66.95
#             n = t / y
#             print("Available ", n, " yuan")
#         else:
#             print(" Error")
#         self.b = self.b - t
#     def balance(self):
#         print("Available tenge: ", self.b )
#
# m = Money_converter()
# m.money()
# m.convert()
# m.balance()

