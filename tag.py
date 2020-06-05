import json
from urllib.request import urlopen

data = urlopen("https://api.github.com/repos/denoland/deno/releases/latest").read()
res = json.loads(data)
print(res["tag_name"], end="")
