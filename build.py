print("test top of python script")
# Combine top middle bottom for index.html
start = open("templates/top.html").read()
middle = open("content/index.html").read()
end = open("templates/bottom.html").read()
combined = start + middle + end
open("docs/index.html", "w+").write(combined)

# combine top middle bottom for about.html
start = open("templates/top.html").read()
about = open("content/about.html").read()
end = open("templates/bottom.html").read()
new_about_page = start + about + end
open("docs/about.html", "w+".write(new_about_page)

# combine top middle bottom for photography.html
# To do:
# 1. copy about.html, contact.html to content directory.- DONE
# 2. remove top and bottom from content/photography.html (DONE), content/about.html (DONE), content/projects.html (DONE)
# and music.html (DONE) content/contact.html (DONE).

# TO BE DONE:
# 3. write additional bash(DONE) and python code to combine above HTML files with top.html and bottom.html
#
print("test bottom part of python script")
