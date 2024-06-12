
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import os
import warnings
warnings.filterwarnings("ignore")

class BlenderBot:
    def __init__(self, model_path):
        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_path)
        self.history = []
    
    def __call__(self, inputs: str):
        
        self.history.append(inputs)
        
        if len(self.history) > 5:
            history_c = self.history[-5:]
        else: 
            history_c = self.history
            
        inputs_tokenized = self.tokenizer("\n".join(history_c), return_tensors='pt', truncation=True, max_length=128)
        
        outputs = self.model.generate(**inputs_tokenized)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        self.history.append(response)
        return response
