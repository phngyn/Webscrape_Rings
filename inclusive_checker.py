import os

dir_path = os.path.dirname(os.path.realpath(__file__))

ring_src = dir_path + "\\ring_src.txt"
ring_data = dir_path + "\\ring_data.txt"

with open(ring_src) as f:
    ring_src_lines = [line.rstrip() for line in f]

with open(ring_data) as g:
    ring_data_lines = [line.rstrip() for line in g]

# print(ring_data_lines)

for line in ring_src_lines:
    with open(ring_data) as data:
        if line in data.read():
            print("True")