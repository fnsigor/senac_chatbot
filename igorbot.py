from datetime import time
import time
time.clock = time.time # ccorrige o erro de time.clock
from chatterbot import ChatBot

#chatbot é a declaracao de uma variavel
chatbot = ChatBot("IgorChatBot")

#variavel que recebe uma array
sairdobot = (":q", "quit", "exit", "sair")

while True:
    query = input("> ")
    if query in sairdobot:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")