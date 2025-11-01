# Configuration file for the Sphinx documentation builder.

import sys
import os

project = 'Aeternum'
copyright = '2025, Santiago Tuta'
author = 'Santiago Tuta'
release = 'Aeternum'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# Tema
html_theme = 'furo'
html_static_path = ['_static']

# Logo del proyecto
html_logo = "_static/aeternum_logo.png"

# Título que aparece en la pestaña del navegador
html_title = "Aeternum - Documentación"

# Opciones del tema Furo
html_theme_options = {
    "sidebar_hide_name": True,  # Oculta el texto del proyecto para que solo se vea el logo
    "light_logo": "aeternum_logo.png",  # Logo modo claro
}
