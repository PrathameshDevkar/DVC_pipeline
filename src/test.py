# from sklearn.feature_extraction.text import TfidfVectorizer

# corpus = [
#     "The sky is blue",
#     "The sun is bright",
#     "The sun in the sky is bright",
#     "We can see the shining sun, the bright sun"
# ]

# # Keep only top 5 most frequent words
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)

# print(X)
# print(vectorizer.get_feature_names_out())
# print(X.toarray())

import os
import numpy as np
import pandas as pd
import pickle
import logging
from sklearn.ensemble import RandomForestClassifier
import yaml