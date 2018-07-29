
import string
import re

import numpy as np
import pandas as pd

raw_data = pd.read_("./data/processed/training_data copy.").drop_duplicates().fillna("This is None")

# write output to these files (train & test)
train_from = open("./data/processed/train.from", "w")
train_to = open("./data/processed/train.to", "w")
test_from = open("./data/processed/test.from", "w")
test_to = open("./data/processed/test.to", "w")

def clean(text):
    chars = re.escape(string.punctuation)
    text = re.sub(r'['+chars+']', '',text)
    text = text.replace("\n","")
    text = text.replace("\r","")
    return text.replace('"',"'")

def run(raw_data):    
    raw_data = raw_data.dropna()
    

    # split data into train and test
    row_count = raw_data.shape[0]
    test_count = int(row_count * (30/100))
    train_count = row_count - test_count
    train_f = raw_data["title_content"][:train_count]
    train_t = raw_data["comment"][:train_count]
    test_f = raw_data["title_content"][train_count:]
    test_t = raw_data["comment"][train_count:]

    # write the data to output files
    for row in train_f.values:
        row = clean(row)
        train_from.write(row+"\n")
    for row in train_t.values:
        row = clean(row)
        train_to.write(row+"\n")        
    for row in test_f.values:
        row = clean(row)
        test_from.write(row+"\n") 
    for row in test_t.values:
        row = clean(row)
        test_to.write(row+"\n")         

    train_from.close()
    train_to.close()
    test_from.close()
    test_to.close()

def print_size():
    print(len(open("./data/processed/train.from","r").readlines()), len(open("./data/processed/train.to","r").readlines()))
    print(len(open("./data/processed/test.from","r").readlines()), len(open("./data/processed/test.to","r").readlines()))

            
if __name__ == "__main__":
    run(raw_data)
    print_size()