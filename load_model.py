#from blenderbot import BlenderBot
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration


# # Load model base
model_name = 'facebook/blenderbot-400M-distill'
tokenize_name = 'facebook/blenderbot-400M-distill'
model_path = 'model/blenderBot'

print("model base is installing...")
BlenderbotForConditionalGeneration.from_pretrained(model_name).save_pretrained(model_path)
BlenderbotTokenizer.from_pretrained(tokenize_name).save_pretrained(model_path)
print("model base is installed")

# Load model fine tunning
model_name_fine_tunning = 'QuanHcmus/results'
tokenize_name_fine_tunning = 'facebook/blenderbot-400M-distill'
model_path_tunning = 'model/blenderBot_fine_tunning'

print("model fine tunning is installing...")
BlenderbotForConditionalGeneration.from_pretrained(model_name_fine_tunning).save_pretrained(model_path_tunning)
BlenderbotTokenizer.from_pretrained(tokenize_name_fine_tunning).save_pretrained(model_path_tunning)
print("model fine tunning is installed")

def response(input, model_path):
    print("model is loading...")
    model = BlenderbotForConditionalGeneration.from_pretrained(model_path)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_path)   
    print("model is loaded")
    input = tokenizer(input, return_tensors='pt', truncation=True, max_length=128)
    output = model.generate(**input)
    print(tokenizer.decode(output[0], skip_special_tokens=True))


while True:
    input_1 = "hello, i'm Quan"
    # input_2 = "how do you feel today"
    # input_3 = "where do you live ?"
    response(input_1, model_path)
    #response(input_1, model_path_tunning)
    
    # print(model(input_2))
    # print(model(input_3))
    break
