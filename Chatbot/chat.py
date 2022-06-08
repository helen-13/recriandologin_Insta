#Import as bibliotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Nomeie o seu chat
chatbot = ChatBot('Queen Skull')

#Construção de conversa para o chat
conversation = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
			'Qual o seu nomer?', 'Helen']

response = chatbot.get_response('I would like to book a flight.')

print(response)

trainer = ListTrainer(chatbot)
trainer.train(conversation)


