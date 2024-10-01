import os
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = Path(current_dir).parent

print(current_dir)
print(parent_dir)