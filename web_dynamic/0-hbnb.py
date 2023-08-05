#!/bin/bash

# Copy files and folders
cp -r web_flask/static web_dynamic/
cp -r web_flask/templates/100-hbnb.html web_dynamic/templates/0-hbnb.html
cp web_flask/__init__.py web_dynamic/
cp web_flask/100-hbnb.py web_dynamic/0-hbnb.py

# Update route in 0-hbnb.py
sed -i 's@app.route("/0-hbnb/")@app.route("/")@g' web_dynamic/0-hbnb.py

# Check if 100-hbnb.html exists, if not use 8-hbnb.html
if [ ! -f web_dynamic/templates/0-hbnb.html ]; then
    cp web_flask/templates/8-hbnb.html web_dynamic/templates/0-hbnb.html
fi

echo "Setup complete."
