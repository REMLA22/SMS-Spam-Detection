# File:        text_preprocess.py
#
# Author:      Rohan Patel
#
# Date:        05/09/2018
#
# Description: This script loads the sms spam data, organizes the data into a pandas dataframe, adds a new 
#              feature (length of message) to the data, and applies some basic text pre-processing techniques 
#              like stopword removal and punctuation removal. Finally, the processed dataframe is copied into 
#              a new csv file processed_msgs.csv

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def loadData():
    
    messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t', names = ['label', 'message'])
    messages['length'] = messages['message'].apply(len)
    
    return messages

def text_process(data):
    '''
    1. remove punc
    2. remove stop words
    3. return list of clean text words
    '''
    
    nopunc = [c for c in data if c not in string.punctuation] #remove punctuations
    nopunc = ''.join(nopunc)
    
    #nltk.download('stopwords')
    clean_msgs = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')] # remove stopwords
    
    return clean_msgs

def main():
    
    messages = loadData()
    #print(messages)
    messages['message'] = messages['message'].apply(text_process)
    
    print('\n######################## Processed Messages #########################\n')
    print(messages)
    messages.to_csv('output/processed_msgs.csv', encoding='utf-8', index=False) #copy processed messages dataframe to a new csv file

if __name__ == "__main__":
    main()