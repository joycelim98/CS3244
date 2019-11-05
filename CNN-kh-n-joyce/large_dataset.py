"""
Function calls to read data from jsonl file, and to present data in a pandas data frame
"""
import jsonlines
import numpy as np
import os
import pandas as pd

# to read extracted data from jsonl file
def read_data(fileName, cutoff = None):
    data = [["", "id", "title", "description", "content", "keywords", "truthMean", "truthMedian", "truthMode", "label"]]
    count = 1
    
    with jsonlines.open(fileName) as reader:
        for obj in reader:
            instance_id = obj["id"]
            title = obj["title"]
            description = obj["description"]
            content = obj["content"]
            keywords = obj["keywords"]
            truthMean = obj["truthMean"]
            truthMedian = obj["truthMedian"]
            truthMode = obj["truthMode"]
            label = obj["label"]

            instance = [count, instance_id, title, description, content, keywords, truthMean, truthMedian, truthMode, label]
            data.append(instance)
            count += 1
            if cutoff != None:
                if count > cutoff:
                    break

    data = np.array(data)
    return data

# to get data packaged as pandas dataframe
def get_data(fileName, cutoff = None):
    # gets raw data as a np array
    if cutoff:
        data_raw = read_data(fileName, cutoff)
    else:
        data_raw = read_data(fileName)

    # convert np array into pandas dataframe
    data = pd.DataFrame(data=data_raw[1:, 1:],
                        index=data_raw[1:, 0],
                        columns=data_raw[0, 1:])

    return data

def get_large_dataset(cutoff = None):
    parent_dir = os.path.dirname(os.getcwd())
    grandparent_dir = os.path.dirname(parent_dir)

    fileName = os.path.join(parent_dir, "InitialDataset/instances_extracted_large.jsonl")
    if cutoff:
        return get_data(fileName, cutoff = cutoff)
    return get_data(fileName)

