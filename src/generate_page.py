import os
import shutil

from copy_static_files import *
from extract_title import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        from_path_contents = f.read()
    
    with open(template_path) as f:
        template_path_contents = f.read()

    from_path_HTML = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)
    template_with_title = template_path_contents.replace("{{ Title }}", title)
    full_page = template_with_title.replace("{{ Content }}", from_path_HTML)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(full_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
         if dir_path_content.endswith(".md"):
             
             relative_path = os.path.relpath(dir_path_content, "content")
             output_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
             os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
             generate_page(dir_path_content, template_path, output_file_path)
    
    elif os.path.isdir(dir_path_content):
        for entry in os.listdir(dir_path_content):
            from_path = os.path.join(dir_path_content, entry)
            if os.path.isdir(from_path):
                generate_pages_recursive(from_path, template_path, dest_dir_path)
            elif entry.endswith(".md"):
                relative_path = os.path.relpath(from_path, "content")
                output_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                generate_page(from_path, template_path, output_file_path)