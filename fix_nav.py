import os
import re

nav_links = """        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about.html">About</a></li>
            <li><a href="/leadership/">Leadership</a></li>
            <li><a href="/projects.html">Projects</a></li>
            <li><a href="/resume/">Resume</a></li>
            <li><a href="/cv/">CV</a></li>
            <li><a href="/research/">Research</a></li>
            <li><a href="/press/">Press</a></li>
            <li><a href="/contact.html">Contact</a></li>
        </ul>"""

html_files = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".html") or f.endswith(".htm"):
            html_files.append(os.path.join(root, f))

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace anything between <ul class="nav-links"> and </ul>
    new_content = re.sub(
        r'<ul class="nav-links">.*?</ul>',
        nav_links,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated navigation in {path}")
