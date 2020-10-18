"""
This is a program for a chat bot......

1. the bot will start with a greeting nd sk for name odf the person
2 bot will greet and welcome the person
3.bor will ask what a person want to do it will offer a choice of thing based upon what the bot is designed for
4.it will respond to users input approximately
"""
import random
from datetime import datetime

def greeting():
    response=[
        "Hi.. My name is Bot. How can I help you. May I know your Name?",
        "Hello..My name is Bot. My I know your Name ? ",
        "Hi... This is Bot.I helps todo some calculations and May I know ur name"
    ]
    print(random.choice(response))
def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour >= 22:
        timeofday_greeting = " sorry! it's too late "
    elif current_time.hour >= 17 :
        timeofday_greeting = "Good Evening"
    elif current_time.hour >= 12:
        timeofday_greeting = "Good afternoon"
    return timeofday_greeting
def welcome(name):
    messages=[
        "nice to meet you",
         "Lets have some good time together"
    ]
    print( "Hi "+  name+" "f"{get_timeofday_greeting()}, {random.choice(messages)}")

def show_menu():
    print("***************************************")
    print("<----------------Select an your choice---------------->")
    print("1. Calculate an expression")
    print("2. Get current time")
    print("3. End this chat")
    print("***************************************")
    try:
        return int(input("Enter your choice [1-3] : "))
    except :
        print(" Only enter from 1,2 and 3")
        return 0
def evaluate_expression():
    expr=input("Enter an expression")
    try:
        print("Result=",eval(expr))
    except Exception as e:
        print(str(e))
def bot():
    greeting()
    name=input("Enter your name please : ")
    welcome(name)
    choice=show_menu()
    while choice !=3:
        if choice==1:
            evaluate_expression()
        elif choice==2:
            print(str(datetime.now()))
        else:
            print("I dont understand that")
        choice=show_menu() 
bot()


