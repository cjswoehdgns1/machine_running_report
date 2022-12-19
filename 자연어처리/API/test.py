from train import train_sentences
from return_sentence import return_similar_answer

model, train_data  = train_sentences(200)

'''this is return test code'''

sample_arr = [
  "결혼하고싶어", 
  "나랑 커피먹을래?", 
  "반가워", 
  "사랑해", 
  "너는 누구니?", 
  "영화", 
  "너무 짜증나", 
  "화가납니다", 
  "나랑 놀자", 
  "나랑 게임하자", 
  "출근하기싫어", 
  "여행가고싶다", 
  "너 말 잘한다"
]

for i in sample_arr:
  print(return_similar_answer(model, train_data, i))