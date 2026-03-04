import base64

with open("./src/fonts/NotoSansDevanagari-Regular.ttf", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

with open("./src/fonts/NotoSansDevanagari.js", "w") as f:
    f.write(f'export const font = "{data}";\n')

print("Done! NotoSansDevanagari.js created successfully.")
