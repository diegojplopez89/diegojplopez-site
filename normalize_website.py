import os
from bs4 import BeautifulSoup

# Standardized blocks based on index.html
PRIMARY_NAV_HTML = """<a href="/about.html">About</a><a href="/capabilities/">Capabilities</a><a href="/leadership/">Experience</a><a href="/projects.html">Systems</a><a href="/resume/">Resume &amp; CV</a><a href="/research/">Research</a><a href="/press/">Press</a><a href="/contact.html">Contact</a>"""

FOOTER_LINKS_HTML = """<a href="/about.html">About</a><a href="/capabilities/">Capabilities</a><a href="/leadership/">Experience</a><a href="/projects.html">Systems</a><a href="/resume/">Resume &amp; CV</a><a href="/clinical/">Clinical</a><a href="/research/">Research</a><a href="/speaking/">Speaking</a><a href="/recognition/">Recognition</a><a href="/press/">Press</a><a href="/contact.html">Contact</a>"""

def get_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                yield os.path.join(root, file)

for filepath in get_html_files('.'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    
    # 1. Normalize Primary Navigation
    nav = soup.find('nav', {'aria-label': 'Primary navigation'})
    if nav:
        new_nav_soup = BeautifulSoup(PRIMARY_NAV_HTML, 'html.parser')
        if str(nav.decode_contents()) != str(new_nav_soup):
            nav.clear()
            for child in new_nav_soup.children:
                nav.append(child)
            changed = True
            
    # 2. Normalize Footer Links
    footer = soup.find('div', class_='footer-links')
    if footer:
        new_footer_soup = BeautifulSoup(FOOTER_LINKS_HTML, 'html.parser')
        if str(footer.decode_contents()) != str(new_footer_soup):
            footer.clear()
            for child in new_footer_soup.children:
                footer.append(child)
            changed = True

    # 3. Inject Open Graph Tags if missing
    head = soup.find('head')
    if head:
        og_tags = [
            {'property': 'og:type', 'content': 'website'},
            {'property': 'og:image', 'content': 'https://diegojplopez.com/assets/Images/Diego1.jpeg'},
            {'name_attr': 'twitter:card', 'content': 'summary_large_image'}
        ]
        for tag_info in og_tags:
            key = 'property' if 'property' in tag_info else 'name'
            lookup_val = tag_info['property'] if 'property' in tag_info else tag_info['name_attr']
            existing = head.find('meta', {key: lookup_val})
            if not existing:
                if key == 'property':
                    new_meta = soup.new_tag('meta', property=lookup_val, content=tag_info['content'])
                else:
                    new_meta = soup.new_tag('meta', attrs={"name": lookup_val, "content": tag_info['content']})
                head.append(new_meta)
                changed = True
                
        # Ensure og:title exists
        if not head.find('meta', {'property': 'og:title'}):
            title_tag = head.find('title')
            page_title = title_tag.text if title_tag else 'Diego Javier Piña Lopez | Humanitarian & Nonprofit Leader'
            new_meta = soup.new_tag('meta', property='og:title', content=page_title)
            head.append(new_meta)
            changed = True

    if changed:
        # Write back
        # BS4 can mess up formatting, so let's use the standard formatter or just output
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Normalized {filepath}")

print("Normalization complete.")
