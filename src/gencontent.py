import os
from block_markdown import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(source_path):
            if source_path.endswith("md"):
                # change filename.md to filename.html
                dest_path = dest_path.replace(".md", ".html")
                with open(source_path, 'r') as f:
                    markdown_content = f.read()
                with open(template_path, 'r') as f:
                    template_content = f.read()
                html_str = markdown_to_html_node(markdown_content).to_html()
                title = extract_title(markdown_content)

                final_html = template_content.replace("{{ Title }}", title)
                final_html = final_html.replace("{{ Content }}", html_str)

                dest_dir = os.path.dirname(dest_path)

                if dest_dir:
                    os.makedirs(dest_dir, exist_ok=True)

                with open(dest_path, 'w') as f:
                    f.write(final_html)
        else:
            generate_pages_recursive(source_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as f:
        template_content = f.read()
    html_str = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_str)

    dest_dir = os.path.dirname(dest_path)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(final_html)


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:]
    raise Exception("No h1 header found")