from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Demon')

trainer = ListTrainer(chatbot)

trainer.train([
    "你好",
    "我很好，你呢",
    "还行"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('你呢')

print(response)