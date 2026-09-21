# board.py - team knowledge board
# run with:  python board.py
# (run it from inside the cloned repo folder)

import os
from datetime import datetime

# make sure the entries folder exists
os.makedirs("entries", exist_ok=True)

# get everyone else's entries first
print("Getting latest entries...")
os.system("git pull")
print()

# ask the questions
name = input("Your name: ").strip()
while name == "":
    name = input("Name can't be empty. Your name: ").strip()

pr = input("PR you're working on (number, or just press enter for none): ").strip()
while pr != "" and not pr.lstrip("#").isdigit():
    pr = input("That's not a number. PR number (or enter for none): ").strip()

partners = input("Who are you working with? ").strip()
area = input("What area is this in (frontend, backend, database, testing...)? ").strip()
stuck = input("What are you stuck on? ").strip()
learned = input("What did you learn recently? ").strip()
can_help = input("What can you help others with? ").strip()

# fill in blanks
if pr == "":
    pr = "none"
else:
    pr = "#" + pr.lstrip("#")
if partners == "":
    partners = "nobody"

# build the entry text
date = datetime.now().strftime("%Y-%m-%d %H:%M")
entry = "## " + name + " (" + date + ")\n"
entry += "- **PR:** " + pr + "\n"
entry += "- **Working with:** " + partners + "\n"
entry += "- **Area:** " + area + "\n"
entry += "- **Stuck on:** " + stuck + "\n"
entry += "- **Learned:** " + learned + "\n"
entry += "- **Can help with:** " + can_help + "\n\n"

# save it to this person's own file (so nobody edits the same file)
filename = "entries/" + name.lower().replace(" ", "_") + ".md"
with open(filename, "a", encoding="utf-8") as f:
    f.write(entry)

# rebuild README.md by sticking all the entry files together
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# Team Knowledge Board\n\n")
    for file in sorted(os.listdir("entries")):
        if file.endswith(".md"):
            with open("entries/" + file, "r", encoding="utf-8") as f:
                readme.write(f.read())
            readme.write("---\n\n")

# send it to github
os.system("git add entries README.md")
os.system('git commit -m "new entry"')
os.system("git push")

print()
print("Done! Check the repo on GitHub to see the board.")