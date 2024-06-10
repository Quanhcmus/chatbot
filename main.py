from blenderbot import BlenderBot


model_name = 'facebook/blenderbot-400M-distill'
model_path = 'model/blenderBot'

while True:
    input_1 = "hello, i'm Quan"
    input_2 = "how do you feel today"
    input_3 = "where do you live ?"
    
    print("model is loading...")
    bot = BlenderBot(model_name, model_path)
    print("model is loaded")
    
    print(bot(input_1))
    print(bot(input_2))
    print(bot(input_3))
    break
print("history conversation:\n", bot.history)