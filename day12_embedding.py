import os
import numpy as np
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") # 384 size model
text = "Machine Learning is fun."

# embedding = model.encode(text)
# print(embedding.shape)
# print(embedding[:10])


def cosine_similarity(a, b):
    return np.dot(a, b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

t1 = "There are 24 paid leaves"
t2 = "There are 24 paid leaves"

v1 = model.encode(t1)
v2 = model.encode(t2)

print(cosine_similarity(v1, v2))