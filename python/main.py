# chatbot
isRunning = True
while isRunning == True:
    UI = input("Hello, I'm chatbot, ask anything what you ever want: ")

    if UI == "Hello":
        UI = input("Hello, how are you?")
        if UI == "good" or UI == "I'm fine" or UI == "Good" or UI == "it going well":
            print("i am glad too hear that")
        elif UI == "bad" or UI == "I'm not very well":
            UI = input("what is wrong?")

    if UI == "Can you calcutlaate something for me?" or UI == "sum" or UI == "calculate" or UI == "Sum":
        # number one
        x = input("Take number one: ")
        xValue = int(x)

        # changing
        changingToCalculate = input("put something to calculate with: ")

        # number two
        y = input("Take another number: ")
        yValue = int(y)

        if changingToCalculate == "-":
            print(xValue - yValue)
        elif changingToCalculate == "/":
            print(xValue / yValue)
        elif changingToCalculate == "+":
            print(xValue + yValue)
        elif changingToCalculate == "*" or changingToCalculate == "x" or changingToCalculate == "X":
            print(xValue * yValue)



    if UI == "What is th time today?" or UI == "What is it today?":
        currentTime = datetime.datetime.now()
        formattedTime = currentTime.strftime("%H:%M:%S")
        print(f"the current time is {formattedTime}")
    elif x == "time":
        currentDate = datetime.datetime.now()
        formattedDate = currentTime.strftime("%Y/%m/%d")
        print(f"the current date is {formattedDate}")
    elif x == "both":
        currentTime = datetime.datetime.now()
        formattedTime = currentTime.strftime("%H:%M:%S")
        currentDate = datetime.datetime.now()
        formattedDate = currentTime.strftime("%Y/%m/%d")
        print(f"the current moment is {formattedTime} {formattedDate}")
    
    