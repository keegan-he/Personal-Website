start = open("templates/top.html").read()
middle = open("content/index.html").read()
end = open("templates/bottom.html").read()
open("docs/index.html", "w+").write(full)