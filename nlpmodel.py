from datasets import load_dataset

dataset = load_dataset("aelhalili/bash-commands-dataset")
print(dataset)
print(dataset['train'][0])  # check first record

#Preprocessing for Auto-completion

def make_autocomplete_pairs(example):
    text=example["prompt"]
    words=text.split()
    pairs=[]
    for i in range(1,len(words)):
        partial=" ".join(words[:i])
        pairs.append({"input_text":partial,"target_text":text})

    return pairs
# Expand dataset 
from itertools import chain 
def expand_dataset(dataset): 
    expanded = list(chain.from_iterable(make_autocomplete_pairs(ex) for ex in dataset)) 
    return expanded 
train_data = expand_dataset(dataset["train"]) 
print(train_data[:2]) 