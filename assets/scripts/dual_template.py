#!/usr/bin/env python3
"""
Dual Template Generator
Generates two markdown files from a single Zotero item using two different templates.
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
from pyzotero import zotero
import re


class DualTemplateGenerator:
    def __init__(self, library_id, api_key, library_type='user'):
        """Initialize the generator."""
        self.zot = zotero.Zotero(library_id, library_type, api_key)
    
    def get_item(self, item_id):
        """Fetch a single item from Zotero."""
        return self.zot.item(item_id)
    
    def extract_authors(self, item_data):
        """Extract and format authors from item."""
        creators = item_data.get('creators', [])
        authors = []
        
        for creator in creators:
            if creator.get('creatorType') in ['author', 'contributor', 'interviewer', 
                                               'director', 'guest', 'presenter', 
                                               'performer', 'castMember']:
                first = creator.get('firstName', '')
                last = creator.get('lastName', '')
                name = creator.get('name', '')
                
                if first and last:
                    authors.append(f"{first} {last}")
                elif name:
                    authors.append(name)
        
        return ', '.join(authors) if authors else ''
    
    def format_date(self, date_str):
        """Format date string to YYYY-MM-DD."""
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')
        
        for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y']:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        return date_str if date_str else datetime.now().strftime('%Y-%m-%d')
    
    def slugify(self, text):
        """Convert text to URL-safe slug."""
        import re
        # Convert to lowercase
        text = text.lower()
        # Replace spaces and underscores with hyphens
        text = re.sub(r'[\s_]+', '-', text)
        # Remove non-alphanumeric characters (except hyphens)
        text = re.sub(r'[^a-z0-9\-]', '', text)
        # Remove multiple consecutive hyphens
        text = re.sub(r'-+', '-', text)
        # Remove leading/trailing hyphens
        text = text.strip('-')
        return text
    
    def load_template(self, template_path):
        """Load template file."""
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def populate_template(self, template, item):
        """Populate template with item data."""
        item_data = item['data']
        
        # Get date and title
        date_str = self.format_date(item_data.get('date', ''))
        title = item_data.get('title', 'Untitled')
        title_slug = self.slugify(title)
        
        # Parse date for components
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            year = date_obj.strftime('%Y')
            month = date_obj.strftime('%m')
            day = date_obj.strftime('%d')
        except:
            year = datetime.now().strftime('%Y')
            month = datetime.now().strftime('%m')
            day = datetime.now().strftime('%d')
        
        # Basic replacements
        replacements = {
            '[zotero-id]': item['key'],
            '[title]': title,
            '[title-slug]': title_slug,
            '[%Y-%m-%d]': date_str,
            '[%Y]': year,
            '[%m]': month,
            '[%d]': day,
        }
        
        # Author replacement
        template = re.sub(r'authors:\s*""', 
                         f'authors: "{self.extract_authors(item_data)}"', 
                         template)
        
        # Publication title with fallback chain
        publication = item_data.get('publicationTitle', '')
        program = item_data.get('programTitle', '')
        website = item_data.get('websiteTitle', '')
        blog = item_data.get('blogTitle', '')
        
        if not publication:
            if program:
                publication = program
            elif website:
                publication = website
            elif blog:
                publication = blog
        
        if publication:
            template = re.sub(r'publication:\s*""', 
                            f'publication: "{publication}"', 
                            template)
        
        # Program title
        if program:
            template = re.sub(r'program:\s*""', 
                            f'program: "{program}"', 
                            template)
        
        # Abstract
        abstract = item_data.get('abstractNote', '')
        if abstract:
            abstract_clean = abstract.replace('\n', ' ').replace('\r', ' ')
            abstract_clean = abstract_clean.replace('"', '\\"')
            abstract_clean = ' '.join(abstract_clean.split())
            
            if abstract_clean:
                template = re.sub(r'abstract:\s*""', 
                                f'abstract: "{abstract_clean}"', 
                                template)
        
        # URL
        url = item_data.get('url', '')
        if url:
            template = re.sub(r'publication-url:\s*""', 
                            f'publication-url: "{url}"', 
                            template)
        
        # DOI
        doi = item_data.get('DOI', '')
        if doi:
            template = re.sub(r'doi:\s*""', 
                            f'doi: "{doi}"', 
                            template)
        
        # Create professional citation
        citation_parts = []
        
        authors = self.extract_authors(item_data)
        if authors:
            citation_parts.append(authors)
        
        if publication:
            citation_parts.append(f"*{publication}*")
        
        # Use date_str already defined at top of method
        if date_str:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                formatted_date = date_obj.strftime('%d %B %Y')
                citation_parts.append(formatted_date)
            except:
                citation_parts.append(date_str)
        
        if citation_parts:
            citation = '. '.join(citation_parts) + '.'
        else:
            citation = ""
        
        # Source link
        if url:
            if publication:
                link_text = publication
            else:
                link_text = "Source"
            source_link = f"* [{link_text}]({url})"
        else:
            source_link = ""
        
        # Combine citation and link
        if citation and source_link:
            full_source = f"{citation}\n\n{source_link}"
        elif citation:
            full_source = citation
        elif source_link:
            full_source = source_link
        else:
            full_source = ""
        
        template = template.replace('[source-link]', full_source)
        
        # Apply basic replacements
        for placeholder, value in replacements.items():
            template = template.replace(placeholder, value)
        
        return template
    
    def generate(self, item_id, template1_path, template2_path, output_dir):
        """
        Generate two markdown files from one item using two templates.
        
        Naming convention:
        - Template 1 (link): YYYY-MM-DD-{zotero_id}.md
        - Template 2 (article): {zotero_id}.md
        
        Args:
            item_id: Zotero item ID
            template1_path: Path to first template (link template)
            template2_path: Path to second template (article template)
            output_dir: Output directory
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Fetch item
        print(f"Fetching item {item_id} from Zotero...")
        item = self.get_item(item_id)
        item_type = item['data'].get('itemType')
        title = item['data'].get('title', 'Untitled')
        print(f"✓ Found: {title}")
        print(f"  Type: {item_type}")
        
        # Get date for filename
        date_str = self.format_date(item['data'].get('date', ''))
        
        # Generate first file (link) - with date prefix
        print(f"\nGenerating link file with template: {template1_path}")
        template1 = self.load_template(template1_path)
        markdown1 = self.populate_template(template1, item)
        
        filename1 = f"{date_str}-{item['key']}.md"
        output_path1 = output_dir / filename1
        
        with open(output_path1, 'w', encoding='utf-8') as f:
            f.write(markdown1)
        
        print(f"✓ Created: {output_path1}")
        
        # Generate second file (article) - ID only
        print(f"\nGenerating article file with template: {template2_path}")
        template2 = self.load_template(template2_path)
        markdown2 = self.populate_template(template2, item)
        
        filename2 = f"{item['key']}.md"
        output_path2 = output_dir / filename2
        
        with open(output_path2, 'w', encoding='utf-8') as f:
            f.write(markdown2)
        
        print(f"✓ Created: {output_path2}")
        
        print("\n" + "=" * 70)
        print("SUCCESS! Generated 2 files:")
        print("=" * 70)
        print(f"Link file:    {output_path1}")
        print(f"Article file: {output_path2}")
        print("=" * 70)
        
        return output_path1, output_path2


def main():
    parser = argparse.ArgumentParser(
        description='Generate two markdown files from one Zotero item using two templates.\n'
                    'File naming: Link = YYYY-MM-DD-{id}.md, Article = {id}.md'
    )
    parser.add_argument('--library-id', required=True,
                       help='Your Zotero library ID')
    parser.add_argument('--api-key', required=True,
                       help='Your Zotero API key')
    parser.add_argument('--item', required=True,
                       help='Zotero item ID')
    parser.add_argument('--template1', required=True,
                       help='Path to link template (will create YYYY-MM-DD-{id}.md)')
    parser.add_argument('--template2', required=True,
                       help='Path to article template (will create {id}.md)')
    parser.add_argument('--output-dir', default='./output',
                       help='Output directory (default: ./output)')
    parser.add_argument('--library-type', default='user',
                       choices=['user', 'group'],
                       help='Library type (user or group)')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = DualTemplateGenerator(
        library_id=args.library_id,
        api_key=args.api_key,
        library_type=args.library_type
    )
    
    # Generate files
    try:
        generator.generate(
            item_id=args.item,
            template1_path=args.template1,
            template2_path=args.template2,
            output_dir=args.output_dir
        )
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
