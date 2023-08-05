#!/bin/bash

# Find all .py files in the current directory and its subdirectories
find . -type f -name "*.py" -print0 | while IFS= read -r -d '' file; do
    # Set executable permission on each .py file
    chmod +x "$file"
done
