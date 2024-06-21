import webbrowser

dic = {
    '1':"www.facebook.com",
    '2':"www.google.com",
    '3':"www.github.com",
    '4':"www.chatgpt.com",
}

def firefox():
    for key, value in dic.items():
       print(f"{key}: {value}")
    x = input("Enter desired website: ")
    webbrowser.open(dic[x])

# def firefox():
#     print("hi")