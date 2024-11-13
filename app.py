import cohere

co = cohere.Client(
    api_key="",
)

chat = co.chat(
    message="hello world!",
    model="command"
)

print(chat)
