from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chatbot 101')
chat = ['Hi', 'Hello', 'Fine', 'Great', 'Do you Like Python?', 'I Like Python']

bot.set_trainer(ListTrainer)
bot.train(chat)

while 1==1:
    question = input('User:')
    answer = bot.get_response(question)
    if float (answer.confidence) > 0.5:
        print('Bot:', answer)
    else:
        print("Bot: I don´t have answer for this question yet")
