import os
import json
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = os.path.join(dir_path, "output.json")

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

df = pd.DataFrame(data).to_json("idnid.json")
df = pd.DataFrame(data).to_excel("idnid.xlsx")
# df = pd.DataFrame(data).to_sql("idnid")