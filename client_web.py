import gspread
import time
from time import sleep
import streamlit as st
from random import random

@st.cache_resource
def run():
    gc = gspread.service_account(filename = "./possible-cycle-443116-c1-f25b4cc7ec5c.json")

    sh = gc.open("fun")

    work = sh.get_worksheet(0)
    return work
work = run()
st.title("Order your food")
#user_name = input("enter a user name ")

if "user_name" in st.session_state:
    st.info(f"Username: {st.session_state.user_name} Order number {st.session_state.order_numb}")   
if "user_name" not in st.session_state:
    holder = st.empty()
    user_name = holder.text_input("user name","")
    if not (user_name == ""):
        user = work.col_values(1)
        work.update_acell(f"A{len(user) + 1}",user_name)
        if "user_name" not in st.session_state:
            st.session_state.user_name = user_name
            st.session_state.order_numb = len(user) + 1
        holder.empty()
        st.info(f"Username: {st.session_state.user_name} Order number {len(user) + 1}")
st.write("Your Cart")
order = []
col,col2 = st.columns(2)
ordered = st.button("Order",use_container_width = True)
A = col.button("A",use_container_width = True)
if "A" not in st.session_state:
    st.session_state.A = 0
if A:
    st.session_state.A += 1
col2.subheader(st.session_state.A)
B = col.button("B",use_container_width = True)
if "B" not in st.session_state:
    st.session_state.B = 0
if B:
    st.session_state.B += 1

col2.subheader(st.session_state.B)

C = col.button("C",use_container_width = True)
if "C" not in st.session_state:
    st.session_state.C = 0
if C:
    st.session_state.C += 1

col2.subheader(st.session_state.C)


D = col.button("D",use_container_width = True)
if "D" not in st.session_state:
    st.session_state.D = 0
if D:
    st.session_state.D += 1

col2.subheader(st.session_state.D)
#order = input("give me your orders 1.A \n 2.B \n 3.C \n 4.D \n 5.E (q)uit\n").split()
if ordered: 
    order.append(str(st.session_state.A) + "A")
    order.append(str(st.session_state.B) + "B")
    order.append(str(st.session_state.C) + "C")
    order.append(str(st.session_state.D) + "D")
    #orders = {i: order.count(i) for i in order}
    #order_pretty = [str(j if j > 1 else "") + i for i,j in zip(orders.keys(),orders.values())]
    order_pretty = [i for i in order if not (i[0] == "0")]
    print("your order is", *order_pretty)
    work.update_acell(f"C{st.session_state.order_numb}"," ".join(order_pretty))
    #print("please wait your order number ",len(user) + 1)
    with st.spinner(f"Please wait your order is being prepared {st.session_state.order_numb}"):
        while not (work.acell(f"D{st.session_state.order_numb}").value == "Finished"):
            sleep(2)
    st.balloons()
    @st.dialog("Order complete")
    def order_complete():
        st.write(f"Order finished you can pick it up now.\n Your order number {st.session_state.order_numb}")
        if st.button("Next Order"):
            st.rerun()
    order_complete()
    st.write(f"Order finished you can pick it up now.\n Your order number {st.session_state.order_numb}")
    print("Order finished you can pick up it now")

