import os

script_dir = os.path.dirname(os.path.abspath(__file__))
inf_path = os.path.join(script_dir, 'inf.txt')

with open(inf_path, 'w', encoding='utf-8') as f:
    f.write(os.path.abspath(__file__))