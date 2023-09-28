from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import time
time.clock = time.time # ccorrige o erro de time.clock


#Flask initialisation
app = Flask(__name__)

chatbot=ChatBot('Senac-Palhoça',storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///banco.sqlite3')

# limpa o banco de dados....
#chatbot.storage.drop();
# ============================================================ Em português
# =========================================================================
# --- comentado código do treinamento ------------------------------
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Now, let us train our bot with multiple corpus
# trainer.train("chatterbot.corpus.english.greetings",
#              "chatterbot.corpus.english.conversations" )
# ------------------------------------------------------------------
# *************************************************** treinamento em português
trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.portuguese')
# ****************************************************************************

## outros idiomas
'''
trainer.train('chatterbot.corpus.english')
trainer.train('chatterbot.corpus.spanish')
trainer.train('chatterbot.corpus.german')
'''
# para treinar ----
trainer = ListTrainer(chatbot)


#essa lista cpntem possiveis posiveis perguntas seguidas de respostas
trainer.train([
    'Oi', 'Olá', 'oi', 'Olá', 'vamos comer sushi?', 'Claro! O bruno irá pagar'
])



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    resposta = ""
    response = chatbot.get_response(msg)
    if float(response.confidence) > 0.2:
        resposta = str(response)
    else:
        resposta = "Ainda não aprendi tudo que preciso"
    return resposta

if __name__ == "__main__":
    app.run()
