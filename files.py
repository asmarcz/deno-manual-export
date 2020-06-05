import json

toc = json.loads(open("deno/docs/toc.json").read())

files = []
for cat in toc:
	files.append(cat)
	if "children" in toc[cat]:
		for sub in toc[cat]["children"]:
			files.append(cat + "/" + sub)

for i, f in enumerate(files):
	files[i] = "deno/docs/" + f + ".md"

for f in files:
	print('"' + f + '" ', end='')
