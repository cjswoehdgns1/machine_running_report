from numpy import dot
from numpy.linalg import norm

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def return_similar_answer(model, train_data, input):
  embedding = model.encode(input)
  train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
  return train_data.loc[train_data['score'].idxmax()]['A']