#!/usr/bin/env python3
"""
Convierte RST a Markdown LIMPIO para GitBook
Sin emojis, sin HTML, estilo profesional
"""

import os
import re
from pathlib import Path
import shutil

def clean_emojis(text):
    """Elimina emojis del texto"""
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def convert_rst_to_markdown(rst_content):
    """Convierte RST a Markdown limpio y profesional"""
    
    # Eliminar HTML raw
    rst_content = re.sub(r'\.\. raw:: html.*?(?=\n\n[^\s]|\Z)', '', rst_content, flags=re.DOTALL)
    rst_content = re.sub(r'<div[^>]*>.*?</div>', '', rst_content, flags=re.DOTALL)
    rst_content = re.sub(r'<[^>]+>', '', rst_content)
    
    # Títulos con = (Nivel 1)
    rst_content = re.sub(r'^(.+)\n=+\n', r'# \1\n\n', rst_content, flags=re.MULTILINE)
    
    # Títulos con - (Nivel 2)
    rst_content = re.sub(r'^(.+)\n-+\n', r'## \1\n\n', rst_content, flags=re.MULTILINE)
    
    # Títulos con ^ (Nivel 3)
    rst_content = re.sub(r'^(.+)\n\^+\n', r'### \1\n\n', rst_content, flags=re.MULTILINE)
    
    # Código inline: ``code`` -> `code`
    rst_content = re.sub(r'``([^`]+)``', r'`\1`', rst_content)
    
    # Bloques de código
    def replace_code_block(match):
        lang = match.group(1) if match.group(1) else ''
        code = match.group(2)
        lines = code.split('\n')
        code_clean = '\n'.join(line[3:] if line.startswith('   ') else line for line in lines)
        return f'\n```{lang}\n{code_clean.strip()}\n```\n\n'
    
    rst_content = re.sub(
        r'\.\. code-block:: ?(\w+)?\n\n((?:   .+\n?)+)',
        replace_code_block,
        rst_content
    )
    
    # Imágenes - Convertir a formato GitBook
    rst_content = re.sub(
        r'\.\. image:: _static/(.+?)\n(?:   :alt: (.+?)\n)?(?:   :align: \w+\n)?(?:   :width: \d+px\n)?',
        r'\n![Imagen](.gitbook/assets/\1)\n\n',
        rst_content
    )
    
    rst_content = re.sub(r'\.\. image:: (.+)', r'\n![Imagen](.gitbook/assets/\1)\n', rst_content)
    
    # Links internos: :doc:`texto` -> [texto](texto.md)
    rst_content = re.sub(r':doc:`([^`]+)`', r'[\1](\1.md)', rst_content)
    
    # Links externos
    rst_content = re.sub(r'`([^<]+)\s*<([^>]+)>`_', r'[\1](\2)', rst_content)
    
    # Notas, Tips, Warnings - Estilo GitBook hint
    def replace_note(match):
        content = match.group(1)
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if line.startswith('   '):
                clean_lines.append(line[3:])
            elif line.strip():
                clean_lines.append(line)
        clean_content = '\n'.join(clean_lines).strip()
        return '\n{{% hint style="info" %}}\n{}\n{{% endhint %}}\n\n'.format(clean_content)
    
    rst_content = re.sub(
        r'\.\. note::\s*\n\n((?:   .+\n?)+)',
        replace_note,
        rst_content
    )
    
    def replace_tip(match):
        content = match.group(1)
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if line.startswith('   '):
                clean_lines.append(line[3:])
            elif line.strip():
                clean_lines.append(line)
        clean_content = '\n'.join(clean_lines).strip()
        return '\n{{% hint style="success" %}}\n**Consejo:** {}\n{{% endhint %}}\n\n'.format(clean_content)
    
    rst_content = re.sub(
        r'\.\. tip::\s*\n\n((?:   .+\n?)+)',
        replace_tip,
        rst_content
    )
    
    def replace_warning(match):
        content = match.group(1)
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if line.startswith('   '):
                clean_lines.append(line[3:])
            elif line.strip():
                clean_lines.append(line)
        clean_content = '\n'.join(clean_lines).strip()
        return '\n{{% hint style="warning" %}}\n**Advertencia:** {}\n{{% endhint %}}\n\n'.format(clean_content)
    
    rst_content = re.sub(
        r'\.\. warning::\s*\n\n((?:   .+\n?)+)',
        replace_warning,
        rst_content
    )
    
    # Limpiar TOC
    rst_content = re.sub(r'\.\. toctree::.*?(?=\n\n[^\s]|\Z)', '', rst_content, flags=re.DOTALL)
    
    # Tablas (list-table)
    rst_content = re.sub(
        r'\.\. list-table::.*?\n   :widths: [\d ]+\n   :header-rows: \d+\n\n((?:   \* - .+\n?)+)',
        convert_list_table,
        rst_content,
        flags=re.DOTALL
    )
    
    # Separadores
    rst_content = re.sub(r'^-{4,}$', '\n---\n', rst_content, flags=re.MULTILINE)
    
    # Eliminar emojis
    rst_content = clean_emojis(rst_content)
    
    # Limpiar endpoint cards (HTML)
    rst_content = re.sub(r'<div class="endpoint-card">.*?</div>', '', rst_content, flags=re.DOTALL)
    
    # Limpiar líneas vacías múltiples
    rst_content = re.sub(r'\n{3,}', '\n\n', rst_content)
    
    return rst_content.strip()


def convert_list_table(match):
    """Convierte list-table a Markdown"""
    content = match.group(1)
    rows = content.split('\n   * - ')
    rows = [r.strip() for r in rows if r.strip()]
    
    if not rows:
        return ''
    
    # Header
    header_parts = rows[0].split('\n     - ')
    md_table = '\n| ' + ' | '.join(header_parts) + ' |\n'
    md_table += '| ' + ' | '.join(['---'] * len(header_parts)) + ' |\n'
    
    # Rows
    for row in rows[1:]:
        cells = row.split('\n     - ')
        md_table += '| ' + ' | '.join(cells) + ' |\n'
    
    return md_table + '\n'


def create_summary(rst_files, output_dir):
    """Crea SUMMARY.md"""
    
    titles = {
        'index': 'Introducción',
        'introduccion': 'Sobre Aeternum',
        'instalacion': 'Instalación',
        'arquitectura': 'Arquitectura',
        'auth_routes': 'Autenticación',
        'password_reset': 'Recuperación de Contraseña',
        'usuario': 'Módulo de Usuario',
        'perfil': 'Gestión de Perfil',
        'wishlist': 'Lista de Deseos',
        'catalogo': 'Catálogo',
        'prestamos': 'Sistema de Préstamos',
        'reviews': 'Reviews y Calificaciones',
        'administracion': 'Panel de Administración',
        'gestion_prestamos': 'Gestión de Préstamos',
        'backend': 'Backend',
        'frontend': 'Frontend',
        'api': 'API Reference',
        'seguridad': 'Seguridad',
    }
    
    summary = "# Tabla de Contenido\n\n"
    
    sections = {
        '## Comenzando': ['index', 'introduccion', 'instalacion', 'arquitectura'],
        '## Autenticación': ['auth_routes', 'password_reset'],
        '## Módulo de Usuarios': ['usuario', 'perfil', 'wishlist'],
        '## Gestión de Libros': ['catalogo', 'prestamos', 'reviews'],
        '## Administración': ['administracion', 'gestion_prestamos'],
        '## Referencia Técnica': ['backend', 'frontend', 'api', 'seguridad'],
    }
    
    for section, files in sections.items():
        summary += f"\n{section}\n\n"
        for file_stem in files:
            if any(f.stem == file_stem for f in rst_files):
                title = titles.get(file_stem, file_stem.title())
                summary += f"* [{title}]({file_stem}.md)\n"
    
    with open(output_dir / 'SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write(summary)


def create_readme(output_dir):
    """Crea README.md profesional"""
    readme = """# Documentación de Aeternum

**Aeternum** es una plataforma moderna de biblioteca virtual que combina préstamos físicos tradicionales con acceso digital instantáneo.

## Acerca de esta documentación

Esta documentación cubre todos los aspectos de Aeternum:

* **Guías de usuario** - Aprende a usar la plataforma
* **Documentación técnica** - Arquitectura y desarrollo
* **API Reference** - Referencia completa de endpoints
* **Administración** - Gestión del sistema

## Comenzar

* [Introducción](index.md) - Conoce el proyecto
* [Instalación](instalacion.md) - Configura tu entorno
* [API Reference](api.md) - Integra con Aeternum

---

**Desarrollado por:** Santiago Tuta  
**Versión:** 1.0.0  
**Licencia:** MIT
"""
    
    with open(output_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)


def convert_file(rst_file, output_dir):
    """Convierte un archivo RST"""
    
    print(f"  • {rst_file.name}")
    
    try:
        with open(rst_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"    ⚠️  Error: {e}")
        return False
    
    md_content = convert_rst_to_markdown(content)
    md_filename = rst_file.stem + '.md'
    output_path = output_dir / md_filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        return True
    except Exception as e:
        print(f"    ⚠️  Error al guardar: {e}")
        return False


def main():
    """Función principal"""
    
    print("\n" + "=" * 70)
    print("CONVERSOR RST → GITBOOK (VERSIÓN LIMPIA)")
    print("=" * 70 + "\n")
    
    source_dir = Path('source')
    output_dir = Path('gitbook_clean')
    
    if not source_dir.exists():
        print(f"❌ No se encontró la carpeta '{source_dir}'")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    rst_files = list(source_dir.glob('*.rst'))
    
    if not rst_files:
        print(f"⚠️  No hay archivos .rst en '{source_dir}'")
        return
    
    print(f"Encontrados {len(rst_files)} archivos\n")
    
    success = 0
    for rst_file in sorted(rst_files):
        if convert_file(rst_file, output_dir):
            success += 1
    
    print(f"\n✓ Convertidos: {success}/{len(rst_files)}\n")
    
    create_summary(rst_files, output_dir)
    create_readme(output_dir)
    print("✓ Archivos de configuración creados\n")
    
    # Copiar imágenes
    static_dir = source_dir / '_static'
    if static_dir.exists():
        output_static = output_dir / '.gitbook' / 'assets'
        output_static.mkdir(parents=True, exist_ok=True)
        
        for img in static_dir.glob('*'):
            if img.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                shutil.copy2(img, output_static / img.name)
        
        print(f"✓ Imágenes copiadas a {output_static}\n")
    
    print("=" * 70)
    print(f"✅ LISTO: {output_dir.absolute()}")
    print("=" * 70)
    print("\nAhora en GitBook:")
    print("1. Elimina el contenido actual")
    print("2. Import → Arrastra los archivos de 'gitbook_clean'")
    print("3. Personaliza colores en Settings → Appearance\n")


if __name__ == '__main__':
    main()