# Deno Manual to PDF

This is my attempt to make Deno Manual available on my Kindle because my eyes are sore.

It has 20pt font and wraps code blocks so that they fit on the page.

You can either grap PDF from this repository (new versions should get generated weekly with GitHub Actions) or compile yourself the latest version.

You will need pandoc with xelatex.

```
git clone --depth 1 https://github.com/asmarcz/deno-manual-export
cd deno-manual-export
# clone the version of docs you want
git clone --depth 1 https://github.com/denoland/deno
python3 gen.py
```
