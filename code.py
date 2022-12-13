!pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from transformers import BertTokenizer, BertModel
import numpy as np
from sentence_transformers.util import cos_sim
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

model = SentenceTransformer('bert-base-multilingual-cased')

#cosine similarity

words = [
#enter words/sentences here
]

vectors = model.encode(words)

cm = np.zeros((len(vectors),len(vectors)))

for i in range(len(words)):
  cm[i:,i] = cos_sim(vectors[i], vectors[i:])
  
colormap = sns.color_palette("Pastel2")

sns.heatmap(cm, annot=True, cmap=colormap)

#MSE

word1 = []
word2 = []

vector1 = model.encode(word1)
vector2 = model.encode(word2)

mse = mean_squared_error(vector1, vector2)

mse
