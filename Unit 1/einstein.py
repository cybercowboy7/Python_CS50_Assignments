
def main():
    user_input = int(input("m: "))

    conversion(user_input)

def conversion(inputs):
    E = inputs*300000000**2

    print("E: ", E)


main()