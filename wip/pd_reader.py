from datetime import date
import os
import json
import pprint
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = dir_path + "\\data_output.json"

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

df = pd.DataFrame(data).to_clipboard()
