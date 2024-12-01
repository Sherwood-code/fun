import gspread
import time
from time import sleep

gc = gspread.service_account(filename = "possible-cycle-443116-c1-f25b4cc7ec5c.json")

sh = gc.open("fun")

work = sh.get_worksheet(0)


user_name = input("enter a user name ")

user = work.col_values(1)
work.update_acell(f"A{len(user) + 1}",user_name)
order = input("give me your orders 1.A \n 2.B \n 3.C \n 4.D \n 5.E (q)uit\n").split()
orders = {i: order.count(i) for i in order}
order_pretty = [str(j if j > 1 else "") + i for i,j in zip(orders.keys(),orders.values())]
print("your order is", *order_pretty)
work.update_acell(f"C{len(user) + 1}"," ".join(order_pretty))
print("please wait your order number ",len(user) + 1)
while not (work.acell(f"D{len(user) + 1}").value == "Finished"):
    sleep(2)
print("Order finished you can pick up it now")
