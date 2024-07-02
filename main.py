from bs4 import BeautifulSoup


def convert_tag(tag):
    assert tag.name, tag
    if tag.name == 'p':
        return f"{convert_children(tag)}\n"
    if tag.name == 'span':
        if "codeBoxLine" in tag.get('class', []):
            return f"{convert_children(tag)}\n"
        else:
            return f"{convert_children(tag)}"
    elif tag.name == 'h1':
        return f"[h1]{convert_children(tag)}[/h1]\n"
    elif tag.name == 'h2':
        return f"[h2]{convert_children(tag)}[/h2]\n"
    elif tag.name == 'h3':
        return f"[h3]{convert_children(tag)}[/h3]\n"
    elif tag.name == 'strong' or tag.name == 'b':
        return f"[b]{convert_children(tag)}[/b]"
    elif tag.name == 'u':
        return f"[u]{convert_children(tag)}[/u]"
    elif tag.name == 'i' or tag.name == 'em':
        return f"[i]{convert_children(tag)}[/i]"
    elif tag.name == 'strike' or tag.name == 'del':
        return f"[strike]{convert_children(tag)}[/strike]"
    elif tag.name == 'a':
        href = tag.get('href')
        if href and tag.get_text():
            return f"[url={href}]{convert_children(tag)}[/url]"
        else:
            return convert_children(tag)
    elif tag.name == 'img':
        src = tag.get('src')
        if src:
            return f"[img]{src}[/img]\n"
        else:
            return ""
    elif tag.name == 'blockquote':
        author = tag.find('div', class_='quoteBoxTitle')
        if author and author.a:
            author_name = author.a.get_text().replace('Zitat von ', '').replace('Quote from ', '')
            return f"[quote={author_name}]\n{convert_children(tag.find('div', class_='quoteBoxContent'))}[/quote]\n"
        else:
            return f"[quote]\n{convert_children(tag)}[/quote]\n"
    elif tag.name == 'ul':
        return f"[list]\n{convert_children(tag)}[/list]\n"
    elif tag.name == 'ol':
        return f"[olist]\n{convert_children(tag)}[/olist]\n"
    elif tag.name == 'li':
        return f"[*]{convert_children(tag)}\n"
    elif tag.name == 'code':
        return f"[code]\n{convert_children(tag)}[/code]\n"
    elif tag.name == 'kbd':
        return f"[b]{convert_children(tag)}[/b]"  # no according steam format for inline code
    elif tag.name == 'table':
        return f"[table]{convert_children(tag)}[/table]\n"
    elif tag.name == 'tr':
        return f"[tr]{convert_children(tag)}[/tr]\n"
    elif tag.name == 'th':
        return f"[th]{convert_children(tag)}[/th]\n"
    elif tag.name == 'td':
        return f"[td]{convert_children(tag)}[/td]\n"
    elif tag.name == 'br':
        return "\n"
    elif tag.name == 'hr':
        return "[hr][/hr]\n"
    elif tag.name == 'div':
        if "codeBoxHeadline" in tag.get('class', []):
            return ""
        return convert_children(tag)
    elif tag.name == 'script' or tag.name == 'noscript':
        return ""
    else:
        return convert_children(tag)


def convert_string(child):
    s = child.string.replace('\n', '')
    if "[" in s or "]" in s:
        return f"[noparse]{s}[/noparse]"
    else:
        return s


def convert_children(tag):
    assert tag.children, tag
    return ''.join(convert_tag(child) if child.name else convert_string(child) for child in tag.children)


with open("input.txt", encoding="utf-8") as f:
    input = f.read()

soup = BeautifulSoup(input, 'html.parser')
steam_output = convert_children(soup).strip()
# print(steam_output)
with open("steam_output.txt", "w", encoding="utf-8") as f:
    f.write(steam_output)
