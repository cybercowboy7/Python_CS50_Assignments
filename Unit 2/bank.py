greeting = input("Greeting: ")

if greeting.startswith(("Hello", "hello")):
    print("$0")
elif greeting.startswith(("h","H"), 0, 1):
    print("$20")
else:
    print("$100")
