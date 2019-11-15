"""
Function calls to read data from jsonl file, and to present data in a pandas data frame
"""
import jsonlines
import numpy as np
import os
import pandas as pd

# to read extracted data from jsonl file
def read_data(fileName):
    data = [["", "content", "label"]]
    count = 1
    
    with jsonlines.open(fileName) as reader:
        for obj in reader:
            content = obj["content"]
            if content == "":
                continue
            label = obj["label"]
            instance = [count, content, label]
            data.append(instance)
            count += 1
    print(len(data))
    data = np.array(data)
    return data

# to get data packaged as pandas dataframe
def get_data(fileName):
    # gets raw data as a np array
    data_raw = read_data(fileName)

    # convert np array into pandas dataframe
    data = pd.DataFrame(data=data_raw[1:, 1:],
                        index=data_raw[1:, 0],
                        columns=data_raw[0, 1:])

    return data

def get_dataset(size = "small"):
    print("loading " + size + " document")
    parent_dir = os.path.dirname(os.getcwd())
    grandparent_dir = os.path.dirname(parent_dir)
    cwd = os.getcwd()
    if size == "small":
        fileName = os.path.join(cwd, "instances_extracted_SMALL.jsonl")
    else:
        fileName = os.path.join(cwd, "instances_extracted_large.jsonl")
    return get_data(fileName)


