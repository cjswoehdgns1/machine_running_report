import urllib.request
import pandas as pd
import os
from sentence_transformers import SentenceTransformer

def train_sentences(ea_cnt):

  if (not os.path.isfile("ChatBotData.csv")):
    urllib.request.urlretrieve(
      "https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv", 
      filename="ChatBotData.csv"
    )
  train_data = pd.read_csv('ChatBotData.csv')
  train_data = train_data.head(ea_cnt)
  model = SentenceTransformer('jhgan/ko-sroberta-multitask')
  train_data['embedding'] = train_data.apply(lambda row: model.encode(row.Q), axis = 1)
  return model, train_data