questions = {"hi":"hello!", "how are you":"I'm good, what about you?", "good bye":"Have a great day, Bye."}
while True:
    Input = input("ME:")
    if Input in questions:
        print("ANSWER: ", questions[Input])
    elif Input == "q":
        break
    else:
        print("Sorry, I'm unable to answer to this.")