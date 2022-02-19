"""
Author - Rakshit RK
Date - Feb 19, 2022
"""





import os
import re
import tensorflow_hub as hub
import numpy as np
from keras.models import load_model
import tensorflow as tf
import keras

## Loading the pre-trained google's word2vec model trained on news and wiki data
embeddings = hub.load("https://tfhub.dev/google/Wiki-words-250/2")
model = load_model(os.getcwd() + '/resources/LSTM_movie_review_classifier.h5')



def remove_punctuations(string):
    punc_pattern = re.compile("["
                              u"\U00000021-\U00000026"  # !"#$%&\'()*+,-./
                              u"\U0000002A-\U0000002A"
                              u"\U0000003A-\U0000003B"
                              u"\U00000040-\U00000040"  # :;<=>?
                              u"\U0000005B-\U00000060"  # [\\]^_`
                              u"\U0000007B-\U0000007F"  # {|}~
                              u"\U00000080-\U0000FFFF"
                              "]+", flags=re.UNICODE)
    text = punc_pattern.sub(r' ', string)
    text = re.sub(" +", " ", text)

    return text


def clean_text(sentence):
    sentence = sentence.replace("-", " ").replace("—", " ")
    sentence = re.sub(r'\(.*\)', "", sentence)
    for sq_br in re.findall(r"\[([A-Za-z0-9_,]+)\]", sentence):
        replace_text = "[" + sq_br + "]"
        sentence = sentence.replace(replace_text, "")
    sentence = remove_punctuations(sentence)
    sentence = re.sub(r'/', ' or ', sentence)
    sentence = re.sub(r'\n', " ", sentence)
    sentence = re.sub('\'', '', sentence)
    # sentence = re.sub('\w*\d\w*', '', sentence)
    sentence = re.sub(r'\n: \'\'.*', '', sentence)
    sentence = re.sub(r'\n!.*', '', sentence)
    sentence = re.sub(r'^:\'\'.*', '', sentence)
    sentence = re.sub(r'\n', ' ', sentence)
    # sentence = re.sub(r'[^\w\s\%]', ' ', sentence)
    sentence = re.sub(r'\   ', " ", sentence)
    sentence = re.sub(r'\-', " ", sentence)
    # sentence = re.sub(r'^https?:\/\/.*[\r\n]*', '', sentence)
    return sentence.strip()


def get_padded_encoded_statements(encoded_text, max_length):
    padded_reviews_encoding = []
    for enc_review in encoded_text:
        zero_padding_cnt = max_length - enc_review.shape[0]
        pad = np.zeros((1, 250))
        for i in range(zero_padding_cnt):
            enc_review = np.concatenate((pad, enc_review), axis=0)
        padded_reviews_encoding.append(enc_review)
    return padded_reviews_encoding


def get_word2vec_enmbeddings(text_list):
    encoded_reviews = []
    for text in text_list:
        tokens = text.split(" ")
        word2vec_embedding = embeddings(tokens)
        encoded_reviews.append(word2vec_embedding)
    return encoded_reviews


def convert_real_text_to_embeddings(text):
    reviews = [text]
    encoded_reviews = get_word2vec_enmbeddings(reviews)
    max_length = 1253  ## Selected from the maximum length sequence present in model training data
    padded_encoded_reviews = get_padded_encoded_statements(encoded_reviews, max_length)
    X = np.array(padded_encoded_reviews)
    return X


def prediction_pipeline(text):
    text = clean_text(text)
    text_embeds = convert_real_text_to_embeddings(text)
    prediction = model.predict(text_embeds)
    output = [1 if val > 0.5 else 0 for val in prediction[0]]
    if np.array(output)[0] == 1:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
    return sentiment


if __name__ == "__main__":
    txt = "The Avengers movie is the greatest movie ever produced in the marvels history"
    print(prediction_pipeline(txt))
