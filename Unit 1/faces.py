
def main():
    user_input = input()
    convert(user_input)

def convert(inputs):
    print(inputs.replace(":)", "🙂").replace(":(", "🙁"))

main()