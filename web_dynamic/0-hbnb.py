import shutil
import os

"""Define the source and destination directories"""
source_dir = "web_flask"
destination_dir = "web_dynamic"

"""Copy the static directory"""
shutil.copytree(os.path.join(source_dir, "static"), os.path.join(destination_dir, "static"))

"""Copy the template directory"""
shutil.copytree(os.path.join(source_dir, "templates"), os.path.join(destination_dir, "templates"))

"""Copy __init__.py"""
shutil.copyfile(os.path.join(source_dir, "__init__.py"), os.path.join(destination_dir, "__init__.py"))

"""Copy 100-hbnb.py and rename it to 0-hbnb.py"""
shutil.copyfile(os.path.join(source_dir, "100-hbnb.py"), os.path.join(destination_dir, "0-hbnb.py"))

"""Check if 100-hbnb.html exists, if not, use 8-hbnb.html"""
if os.path.exists(os.path.join(source_dir, "templates", "100-hbnb.html")):
    shutil.copyfile(os.path.join(source_dir, "templates", "100-hbnb.html"), os.path.join(destination_dir, "0-hbnb.html"))
else:
    shutil.copyfile(os.path.join(source_dir, "templates", "8-hbnb.html"), os.path.join(destination_dir, "0-hbnb.html"))

"""Update 0-hbnb.py to replace the existing route to /0-hbnb/"""
with open(os.path.join(destination_dir, "0-hbnb.py"), "r+") as file:
    content = file.read()
    content = content.replace("/100-hbnb/", "/0-hbnb/")
    file.seek(0)
    file.write(content)
    file.truncate()

"""Start the Flask web application"""
os.system("python3 web_dynamic/0-hbnb.py")
