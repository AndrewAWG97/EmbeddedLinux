#!/bin/python3

import webbrowser

dic = {
    '1':"www.facebook.com",
    '2':"www.google.com",
    '3':"www.yahoo.com",
    '4':"www.chatgpt.com",
}

def firefox():
    x = input("Enter desired website: ")
    webbrowser.open(dic[x])

while(True):
    firefox()


