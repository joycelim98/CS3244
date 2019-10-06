"""
Goal of this script: extract relevant columns, concatenate label for each instance (located in another file)
"""

import jsonlines

data = {}

# extract data
with jsonlines.open('instances_small.jsonl') as reader:
    for obj in reader:
        instance_id = obj["id"]
        title = obj["targetTitle"]
        description = obj["targetDescription"]
        keywords = obj["targetKeywords"]

        data[instance_id] = {
                "id" : instance_id,
                "title" : title,
                "description" : description,
                "keywords" : keywords
                }

# extract truth values
with jsonlines.open('truth.jsonl') as reader:
    for obj in reader:
        instance_id = obj["id"]
        truthMean = obj["truthMean"]
        truthMedian = obj["truthMedian"]
        truthMode = obj["truthMode"]
        truthClass = obj["truthClass"]
        label = 0

        # note that we indicate '1' if truthClass is clickbait
        if truthClass == "clickbait":
            label = 1

        data[instance_id]["truthMean"] = truthMean
        data[instance_id]["truthMedian"] = truthMedian
        data[instance_id]["truthMode"] = truthMode
        data[instance_id]["label"] = label


for key in data:
    print(key)
    for obj in data[key]:
        print(obj, ":", data[key][obj])
    #print("id: %s; content: %s" % (key, value))


output_file = open("instances_extracted.jsonl", "w")
with jsonlines.Writer(output_file) as writer:
    for key in data:
        writer.write(data[key])
output_file.close()


