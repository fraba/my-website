#!/usr/bin/env python3
"""
Zotero Local API to Jekyll Post Generator

This script fetches items from your LOCAL Zotero 7 installation and creates 
Jekyll posts using a predefined template. No API key required!

Requirements:
    pip install pyzotero pyyaml

Setup:
    1. Make sure Zotero 7 is running locally
    2. Get your library ID from Zotero (Settings > General, or check the database)
    3. Update the configuration variables below
    4. Run the script!
"""

from pyzotero import zotero
import yaml
import os
from datetime import datetime
from pathlib import Path
import re


# ==================== CONFIGURATION ====================
# Your Zotero user ID - you can find this in Zotero settings or leave as '0' for local access
ZOTERO_LIBRARY_ID = '0'
ZOTERO_LIBRARY_TYPE = 'user'        # 'user' or 'group'
OUTPUT_DIR = '../../_research-reports'                # Directory where Jekyll posts will be saved

# Specific item to export
SPECIFIC_ITEM_KEY = '4FY3HBJV'  # Replace with your Zotero item key

# Local API settings
LOCAL_API_PORT = 23119  # Default Zotero 7 local API port
# ======================================================


def sanitize_filename(title):
    """Create a valid filename from a title."""
    # Remove or replace invalid characters
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces with hyphens
    title = re.sub(r'\s+', '-', title)
    # Remove multiple hyphens
    title = re.sub(r'-+', '-', title)
    # Limit length
    return title[:100].lower().strip('-')


def get_item_type_category(item_type):
    """Map Zotero item types to your categories."""
    mapping = {
        'journalArticle': 'peer-reviewed journal article',
        'preprint': 'preprint article',
        'conferencePaper': 'conference paper',
        'book': 'book',
        'bookSection': 'book chapter',
        'report': 'research report',
        'thesis': 'thesis',
    }
    return mapping.get(item_type, 'publication')


def format_authors(creators):
    """Format author list from Zotero creators."""
    authors = []
    for creator in creators:
        if creator.get('creatorType') in ['author', 'editor']:
            first_name = creator.get('firstName', '')
            last_name = creator.get('lastName', '')
            if first_name and last_name:
                authors.append(f"{first_name} {last_name}")
            elif last_name:
                authors.append(last_name)
    
    if len(authors) == 0:
        return ""
    elif len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    else:
        # More than 2 authors
        return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def create_jekyll_post(item):
    """Create a Jekyll post from a Zotero item."""
    data = item['data']
    
    # Extract basic information
    title = data.get('title', 'Untitled')
    zotero_key = item['key']
    
    # Get publication date
    date_str = data.get('date', '')
    try:
        # Try to parse various date formats
        if date_str:
            # Extract year-month-day if available
            date_match = re.search(r'(\d{4})-?(\d{2})?-?(\d{2})?', date_str)
            if date_match:
                year = date_match.group(1)
                month = date_match.group(2) or '01'
                day = date_match.group(3) or '01'
                date_obj = datetime(int(year), int(month), int(day))
            else:
                date_obj = datetime.now()
        else:
            date_obj = datetime.now()
    except:
        date_obj = datetime.now()
    
    formatted_date = date_obj.strftime('%Y-%m-%d')
    
    # Format authors
    creators = data.get('creators', [])
    authors = format_authors(creators)
    
    # Get DOI
    doi = data.get('DOI', '')
    
    # Get publication info
    publication = data.get('publicationTitle', '') or data.get('repository', '')
    
    # Get URL
    url = data.get('url', '')
    
    # Get abstract
    abstract = data.get('abstractNote', '')
    
    # Get tags
    tags = [tag['tag'] for tag in data.get('tags', [])]
    
    # Determine category
    item_type = data.get('itemType', '')
    category = get_item_type_category(item_type)
    
    # Create permalink using zotero key
    permalink = f"/{zotero_key}/"
    
    # Build the front matter
    front_matter = {
        'layout': 'single',
        'permalink': permalink,
        'title': title,
        'authors': authors,
        'date': formatted_date,
        'comments': True,
        'published': True,
        'share': True,
        'categories': [category],
        'tags': tags if tags else ['untagged'],
        'doi': doi,
        'publication': publication,
        'publication-url': url,
        'abstract': abstract,
        'excerpt': abstract[:200] + '...' if len(abstract) > 200 else abstract,
    }
    
    # Create the post content
    content = "---\n"
    content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content += "---\n"
    
    # Add publisher link if DOI exists
    if doi:
        content += f"* [Publisher version](https://doi.org/{doi})\n"
    elif url:
        content += f"* [Publisher version]({url})\n"
    else:
        content += "* [Publisher version]()\n"
    
    content += "* [Other links]\n\n"
    content += "Some text\n\n"
    content += "## On social media\n\n"
    
    # Create filename using Zotero item key
    filename = f"{zotero_key}.md"
    
    return filename, content


def main():
    """Main function to fetch Zotero items and create Jekyll posts."""
    print("Connecting to local Zotero instance...")
    print(f"Looking for Zotero on port {LOCAL_API_PORT}...")
    
    try:
        # Initialize Zotero connection with local API
        # Note: api_key can be empty for local connections
        zot = zotero.Zotero(
            ZOTERO_LIBRARY_ID, 
            ZOTERO_LIBRARY_TYPE, 
            api_key='',  # Empty key for local API
            local=True   # Use local API
        )
        
        # Create output directory if it doesn't exist
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
        
        # Fetch specific item by key
        print(f"Fetching item with key: {SPECIFIC_ITEM_KEY}")
        
        try:
            item = zot.item(SPECIFIC_ITEM_KEY)
            items = [item]  # Make it a list for consistent processing
            print(f"Found item: {item['data'].get('title', 'Untitled')}")
        except Exception as e:
            print(f"✗ Error fetching item with key '{SPECIFIC_ITEM_KEY}': {e}")
            print("   Make sure the item key is correct and exists in your library.")
            return
        
        # Process the item
        try:
            filename, content = create_jekyll_post(item)
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            # Write the post
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Created: {filename}")
            print(f"\nSuccess! Jekyll post created in '{OUTPUT_DIR}/{filename}'")
            
        except Exception as e:
            title = item['data'].get('title', 'Unknown')
            print(f"✗ Error processing '{title}': {e}")
    
    except ConnectionError as e:
        print(f"\n✗ Connection Error: Could not connect to local Zotero instance.")
        print(f"   Make sure Zotero 7 is running.")
        print(f"   Error details: {e}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print(f"   Make sure Zotero 7 is running and the local API is enabled.")


if __name__ == "__main__":
    main()
