print("top test")
top_temp = open("templates/top.html").read()
content = open("content/index.html").read()
bottom_temp = open("templates/bottom.html").read()
index_html = top_temp + content + bottom_temp
open("docs/index.html", "w+").write(index_html)
print("bottom test")