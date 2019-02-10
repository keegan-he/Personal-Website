start = open("templates/top.html").read()
middle = open("content/index.html").read()
end = open("templates/bottom.html").read()
combined = start + middle + end
open("docs/index.html", "w+").write(combined)



#To do: 
# 1. copy about.html, contact.html to content directory.- DONE
# 2. remove top and bottom from content/contact.html, content/photography.html, content/about.html, 
# content/projects.html and music.html. 
#3. write additional python and bash to combine above HTML files with top.html and bottom.html
