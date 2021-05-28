from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

train = False
# Create a new chat bot named Charlie
chatbot = ChatBot('Demon')


if train:
    trainer = ListTrainer(chatbot)
    talk_corpus = []
    with open('data/textall4.2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            talk_corpus.append(line.strip())

    trainer.train(talk_corpus)

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('你最喜欢的颜色是什么?')

print(response)