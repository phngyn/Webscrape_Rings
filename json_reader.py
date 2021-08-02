import os
import json
import pprint
dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = dir_path + "\\ring_data.json"

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

ring_round= []
# Gets the value
for entry in data:
    # for j in entry:
    try:
        if (
            entry["field_shape"] == "Round" and
            entry["field_shape"] == "Round"
           ):
            ring_round.append(entry)
            # print(entry["field_shape"])
    except:
        pass

pprint.pprint(ring_round)