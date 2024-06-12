# Create a chatbot for daily conversations with Blenderbot
Fine-tunning blenderbot model to create chatbots for daily conversations and deploy to the web

## Description
The goal of this project is to adjust the Facebook AI-developed BlenderBot model to particular user requirements. BlenderBot is a cutting-edge chatbot made to have intelligent and genuine interactions. Improving the personalized and context-specific responsiveness you offer is made possible by refining this model.
## Getting started
### Dependencies  
+ Data: [dialog.txt](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot?resource=download)
+ Libraries: Flask 2.2.5, Transformers 4.41.2, Pytorch 2.3.0+cu121, Datasets 2.19.2, Tokenizers 0.19.1
### Install
```
git clone https://github.com/Quanhcmus/chatbot.git
```
### Executing program
+ How to run code:  
1. Run main.ipynb to file-tunning model
2. Run main.py to install model from hub to local
3. Run app.py to deloy model to web
+ Step-by-step bullets
1. Open google colab and upload model/dialog.txt, main.ipynb, select TPU(T4) and press ctrl + F9.
2. Inside the main.ipynb file there is code so you can save the new file-tunning model to huggingface, you can customize it to save somewhere else.
```
model_name = 'facebook/blenderbot-400M-distill'

kwargs = {
    "dataset_tags": "marsyas/gtzan",
    "dataset": "GTZAN",
    "model_name": f"{model_name}-finetuned",
    "finetuned_from": model_name,
    "tasks": "audio-classification",
}
```
3. Change the variable **model_name** to the model you saved on huggingface, run main.py to install model
+  To test new models
```
python main.py
```
4. To deloy model run app.py
```
python app.py runserver
```
### Authors
Name: Nguyen Minh Quan
gmail: minhquannguyen20022002@gmail.com
### Refrences
+ [Model](https://huggingface.co/facebook/blenderbot-400M-distill)
+ [Datasets](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot?resource=download)
+ ChatGPT
