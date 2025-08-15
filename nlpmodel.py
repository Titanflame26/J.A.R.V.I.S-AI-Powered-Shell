from datasets import load_dataset

dataset = load_dataset("aelhalili/bash-commands-dataset")
print(dataset)
print(dataset['train'][0])  # check first record
