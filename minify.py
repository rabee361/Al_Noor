#!/usr/bin/env python
"""
Minify CSS, JavaScript, or HTML files and save to the root directory.
Usage: python minify.py path/to/file.css
       python minify.py path/to/directory
"""

import os
import argparse
from pathlib import Path
from csscompressor import compress as compress_css
from jsmin import jsmin
from htmlmin import minify as minify_html

def minify_file(file_path):
    """Minify a file based on its extension and save to root directory."""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist.")
        return False
    
    # Get file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Error: Could not read {file_path} as text. Skipping.")
        return False
    
    # Determine file type and minify accordingly
    ext = file_path.suffix.lower()
    if ext == '.css':
        minified = compress_css(content)
    elif ext == '.js':
        minified = jsmin(content)
    elif ext == '.html':
        minified = minify_html(content, remove_comments=True, remove_empty_space=True)
    else:
        print(f"Error: Unsupported file type {ext}. Supported types: .css, .js, .html")
        return False
    
    # Create output filename (original_name.min.ext)
    output_name = f"{file_path.stem}.min{ext}"
    output_path = Path(os.getcwd()) / output_name
    
    # Save minified content
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(minified)
    
    print(f"Minified {file_path} -> {output_path}")
    print(f"Original size: {len(content):,} bytes")
    print(f"Minified size: {len(minified):,} bytes")
    if content:
        print(f"Reduction: {(1 - len(minified)/len(content))*100:.2f}%")
    
    return True

def process_directory(directory_path):
    """Process all CSS, JS, and HTML files in a directory."""
    directory_path = Path(directory_path)
    
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"Error: Directory {directory_path} does not exist.")
        return False
    
    supported_extensions = ['.css', '.js', '.html']
    files_processed = 0
    
    for ext in supported_extensions:
        for file_path in directory_path.glob(f'**/*{ext}'):
            # Skip already minified files
            if '.min.' in file_path.name:
                continue
                
            if minify_file(file_path):
                files_processed += 1
    
    if files_processed == 0:
        print(f"No CSS, JS, or HTML files found in {directory_path}")
        return False
    
    print(f"Successfully processed {files_processed} files from {directory_path}")
    return True

def main():
    parser = argparse.ArgumentParser(description='Minify CSS, JS, or HTML files')
    parser.add_argument('path', help='Path to the file or directory to minify')
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_dir():
        process_directory(path)
    else:
        minify_file(path)

if __name__ == '__main__':
    main()
