# Configuration file for Sphinx - Estilo GitBook

import sys
import os

# -- Project information
project = 'Aeternum'
copyright = '2025, Santiago Tuta'
author = 'Santiago Tuta'
release = '1.0.0'

# -- General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',  # Botón copiar en código
]

templates_path = ['_templates']
exclude_patterns = []
language = 'es'

# -- HTML output con Sphinx Book Theme (parecido a GitBook)
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
]

html_logo = "_static/aeternum_logo.png"
html_favicon = "_static/favicon.ico"
html_title = "Aeternum Docs"

# Configuración del tema Book (estilo GitBook)
html_theme_options = {
    # Logo y branding
    "logo_only": False,
    "show_toc_level": 2,
    
    # Colores Aeternum
    "repository_url": "https://github.com/Santixxtt/Aeternum",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
    "use_download_button": False,
    
    # Navegación
    "show_navbar_depth": 2,
    "show_prev_next": True,
    
    # Botón custom superior derecha
    "extra_navbar": """
        <div style="margin-left: auto;">
            <a href="https://aeternum.com" 
               target="_blank"
               style="background: linear-gradient(135deg, #FF69B4, #BA8ED9);
                      color: white;
                      padding: 0.5rem 1.5rem;
                      border-radius: 8px;
                      text-decoration: none;
                      font-weight: 600;
                      display: inline-block;
                      transition: all 0.3s ease;">
                Web Aeternum
            </a>
        </div>
    """,
    
    # Búsqueda
    "search_bar_text": "Buscar...",
    
    # Footer
    "extra_footer": """
        <div style="text-align: center; padding: 1rem; color: #888;">
            Hecho con por Santiago Tuta y Mariana Ruiz | © 2025 Aeternum
        </div>
    """,
}

# Pygments (syntax highlighting)
pygments_style = "monokai"

# Opciones adicionales
html_show_sourcelink = False
html_show_sphinx = False

# Búsqueda
html_search_language = 'es'