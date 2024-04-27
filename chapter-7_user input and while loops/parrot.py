# Initial Run:
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# ------------------------------------------------------------

prompt = "Tell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
prompt += "\n: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(f"You said, '{message}'.\n")
