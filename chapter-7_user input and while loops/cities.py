prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' whn you are finished.)"
prompt += "\n: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
