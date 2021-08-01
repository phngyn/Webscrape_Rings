import os
import json
import pprint
dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = dir_path + "\\ring_data.json"

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

# Gets the value
for entry in data:
   for j in entry:
    pprint.pprint(entry)