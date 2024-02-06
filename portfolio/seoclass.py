from django.utils.html import escape
from django.utils.safestring import mark_safe


class SEOClass():


    def __init__(self, title="Welcome to Aman's Dev Lab", description='', keywords='', author='Aman Rawat') -> None:
        if not hasattr(self, 'initialized'):
            self.title = title
            self.description = description
            self.keywords = keywords
            self.author = author    
            self.initialized = True

    def get_meta_tags(self):
        meta_tags = {
            "description": escape(self.description),
            "keywords": escape(self.keywords),
            "author": escape(self.author),
        }

        meta_tags_name = ""

        for name, content in meta_tags.items():
            if content:
                meta_tags_name += f'<meta name="{name}" content="{content}">\n'
        title_tag = f"<title>{self.title} | Kirmola in Lab</title>"
        return mark_safe(f"{title_tag}\n{meta_tags_name}")

    def get_open_graph_tags(self):
        og_tags = {
            'og:title': escape(self.title),
            'og:description': escape(self.description),
            'og:image': "",
            'og:url': "",
            'og:site_name': escape(self.title),
            'og:type': 'website',
            'article:author': escape(self.author),
        }

        og_tags_html = ''
        for property, content in og_tags.items():
            if content:
                og_tags_html += f'<meta property="{property}" content="{content}">\n'

        return mark_safe(og_tags_html)
