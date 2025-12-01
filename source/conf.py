# Configuration file for the Sphinx documentation builder.

import sys
import os

# -- Project information -----------------------------------------------------
project = 'Aeternum'
copyright = '2025, Santiago Tuta'
author = 'Santiago Tuta'
release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']

# CSS personalizado
html_css_files = [
    'custom.css',
]

# Logo del proyecto
html_logo = "_static/aeternum_logo.png"
html_favicon = "_static/favicon.ico"

# Título que aparece en la pestaña del navegador
html_title = "Aeternum Docs"

# Opciones del tema Furo
html_theme_options = {
    "sidebar_hide_name": False,
    
    # Colores personalizados
    "light_css_variables": {
        "color-brand-primary": "#E91E8C",
        "color-brand-content": "#9B59B6",
        "color-admonition-background": "#f8f9fa",
        "font-stack": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
        "font-stack--monospace": "'Fira Code', 'Courier New', monospace",
    },
    
    # Links del footer
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Santixxtt/Aeternum",
            "html": "",
            "class": "",
        },
    ],
    
    # Navegación
    "navigation_with_keys": True,
    
    # Personalización adicional
    "top_of_page_button": "edit",
}

# Configuración de pygments (syntax highlighting)
pygments_style = "monokai"
pygments_dark_style = "monokai"

# Opciones adicionales
html_show_sourcelink = False
html_show_sphinx = False

# Metadatos
html_context = {
    "display_github": True,
    "github_user": "Santixxtt",
    "github_repo": "Aeternum",
    "github_version": "main",
    "conf_py_path": "/docs/",
}