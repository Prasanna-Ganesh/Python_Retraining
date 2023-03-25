from model import task
from flask import json
obj=task(1,"hi","nothing",3)
print(json.dumps(obj))

