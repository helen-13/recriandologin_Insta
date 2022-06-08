
trainer = ListTrainer(chatbot)

trainer.train(['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
			'Qual o seu nomer?', 'Helen',
               ])

response = chatbot.get_response('I would like to book a flight.')

print(response)