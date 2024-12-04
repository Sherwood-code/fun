#our database is google spreadsheets
import gspread #spreadsheet api
import time
from time import sleep

#accessing the spreadsheet
gc = gspread.service_account(filename = "possible-cycle-443116-c1-f25b4cc7ec5c.json")

sh = gc.open("fun")

work = sh.get_worksheet(0)

#enter the user name
user_name = input("enter a user name ")

#generation of order number for each user by allocating the spreadsheet cell thats empty
user = work.col_values(1)
work.update_acell(f"A{len(user) + 1}",user_name)

#getting the user's order
order = input("give me your orders 1.A \n 2.B \n 3.C \n 4.D \n 5.E (q)uit\n").split()
orders = {i: order.count(i) for i in order}
order_pretty = [str(j if j > 1 else "") + i for i,j in zip(orders.keys(),orders.values())]

#printing the user's order the * is to unpack the list to make it look pretty
print("your order is", *order_pretty) # * is called snowflake btw

work.update_acell(f"C{len(user) + 1}"," ".join(order_pretty))
print("please wait your order number ",len(user) + 1)

#checking of the order is done
while not (work.acell(f"D{len(user) + 1}").value == "Finished"):
    sleep(2) #we wait a while to not overflow the api request quota

print("Order finished you can pick up it now")# happy meal
#have a donut
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡤⠤⠤⠤⠤⠴⠶⠶⠦⠤⠤⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠒⠦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀
⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀
⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀
⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀
⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣄⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠢⠤⠴⠿⠽⠟⠓⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⢸⡇⠀⠀⣰⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⠈⡇⠀⢰⠏⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⠀⣿⠀⢻⡀⠀⣧⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠒⡆⣾⡆
⠀⢸⡆⠸⣧⠀⠙⠦⠾⡄⠀⢰⠏⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⢰⣷⠟⡿
⢀⣼⣟⠰⣸⣷⡄⠀⠀⢳⠀⢸⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠶⡄⠀⠀⣰⠛⢳⢀⣇⣰⣋⣸⠞⠁
⣾⠉⢿⣶⡵⣧⣽⣦⡀⠈⢧⢸⡇⠐⣧⠀⠀⢀⣼⠛⠉⠙⠲⣄⠀⠀⠀⠀⠀⠀⢀⡤⠶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⣷⠀⢰⠃⠀⣸⣼⡟⡇⠀⠀⠀⠀
⠘⢷⡄⠉⠉⠈⠉⠀⠙⣦⣬⣿⡃⠀⠸⡄⠀⢸⠇⠀⠀⠀⠀⠈⢧⠀⠀⠀⢀⡴⠋⠀⠀⠀⢷⡄⠀⠀⠀⣤⢶⠄⠀⠀⡼⠀⠀⢠⡏⢀⡏⢀⣴⠟⠛⢡⡇⠀⠀⠀⠀
⠀⠀⠙⠲⠦⠤⠤⠴⠚⠉⢹⣿⣙⣦⠀⠹⠤⠾⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⡾⠀⠀⠀⠀⠀⠀⠻⠦⠴⠚⠁⣸⠀⠀⡼⠁⠀⢀⣾⣅⣼⡗⠋⣧⠤⠾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡉⠋⢛⣶⢤⣀⡀⠀⠀⠀⠀⠀⠀⢸⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣏⣠⡞⢁⣠⣴⣿⣾⠟⠙⠏⢨⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠈⠉⠛⠲⢦⣤⣀⣀⣾⠀⠘⣿⣄⠀⠀⠀⡀⣀⣀⣤⠤⡶⣿⣷⠟⠛⣯⣄⠈⠈⠁⠀⠀⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠈⣹⣻⠀⢀⣻⣿⡟⠛⢹⡏⠉⠉⠉⠓⠗⠚⠁⠀⠀⠀⠉⠓⠚⠛⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠙⠓⠀⠘⠛⠃⠁⣨⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⣄⣀⣠⡤⠶⠛⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
