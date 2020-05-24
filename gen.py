import json
import subprocess

toc = json.loads(open("deno/docs/toc.json").read())

files = []
for cat in toc:
	files.append(cat)
	if "children" in toc[cat]:
		for sub in toc[cat]["children"]:
			files.append(cat + "/" + sub)

for i, f in enumerate(files):
	files[i] = "deno/docs/" + f + ".md"

subprocess.run(["pandoc", "--listings", "--pdf-engine=xelatex", "--resource-path=deno/docs/images", "-o", "deno-manual.pdf", "conf.yml"] + files + ["conf.yml"])
