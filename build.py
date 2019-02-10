start = open("templates/top.html").read()
middle = open("content/index.html").read()
end = open("templates/bottom.html").read()
combined = start + middle + end
open("docs/index.html", "w+").write(combined)

#To do: remove top and bottom from content/photography.html, content/about.html, 
# content/projects.html and music.html. 