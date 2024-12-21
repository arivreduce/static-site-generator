import os, shutil
from copy_files import copy_files_recursive
from generate_page import generate_page
source = "./static"
destination = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
  if os.path.exists(destination):
    shutil.rmtree(destination)
  copy_files_recursive(source, destination)
  print("Generating page...")
  generate_page(
    os.path.join(dir_path_content, "index.md"),
    template_path,
    os.path.join(destination, "index.html"),
  )

main()