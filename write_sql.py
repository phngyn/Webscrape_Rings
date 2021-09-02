from sqlalchemy import create_engine

import pandas as pd
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = os.path.join(dir_path, "idnid.json")

read_json = pd.read_json(ring_data)
df = pd.DataFrame(read_json)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
