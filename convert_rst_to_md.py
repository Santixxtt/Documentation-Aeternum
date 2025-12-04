#!/usr/bin/env python3
"""
Convierte archivos RST de Sphinx a Markdown para GitBook
CORREGIDO: Busca en la carpeta 'source' en lugar de 'docs'
"""

import os
import re
from pathlib import Path
import shutil

def convert_rst_to_markdown(rst_content):
    """Convierte contenido RST a Markdown"""
    
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
        # Eliminar indentación de 3 espacios
        lines = code.split('\n')
        code_clean = '\n'.join(line[3:] if line.startswith('   ') else line for line in lines)
        return f'```{lang}\n{code_clean}```\n\n'
    
    rst_content = re.sub(
        r'\.\. code-block:: ?(\w+)?\n\n((?:   .+\n?)+)',
        replace_code_block,
        rst_content
    )
    
    # Imágenes con atributos completos
    rst_content = re.sub(
        r'\.\. image:: (.+?)\n   :alt: (.+?)\n(?:   :align: \w+\n)?(?:   :width: \d+px\n)?',
        r'![\2](.gitbook/assets/\1)\n\n',
        rst_content
    )
    
    # Imágenes simples
    rst_content = re.sub(r'\.\. image:: (.+)', r'![](.gitbook/assets/\1)\n', rst_content)
    
    # Links internos: :doc:`texto` -> [texto](texto.md)
    rst_content = re.sub(r':doc:`([^`]+)`', r'[\1](\1.md)', rst_content)
    
    # Links externos: `texto <url>`_ -> [texto](url)
    rst_content = re.sub(r'`([^<]+)\s*<([^>]+)>`_', r'[\1](\2)', rst_content)
    
    # Notas
    def replace_admonition(match, hint_type):
        content = match.group(1)
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if line.startswith('   '):
                clean_lines.append(line[3:])
            elif line.strip():
                clean_lines.append(line)
        clean_content = '\n'.join(clean_lines)
        return '\n{{% hint style="{}" %}}\n{}\n{{% endhint %}}\n\n'.format(hint_type, clean_content)
    
    rst_content = re.sub(
        r'\.\. note::\n\n((?:   .+\n?)+)',
        lambda m: replace_admonition(m, 'info'),
        rst_content
    )
    
    rst_content = re.sub(
        r'\.\. tip::\n\n((?:   .+\n?)+)',
        lambda m: replace_admonition(m, 'success'),
        rst_content
    )
    
    rst_content = re.sub(
        r'\.\. warning::\n\n((?:   .+\n?)+)',
        lambda m: replace_admonition(m, 'warning'),
        rst_content
    )
    
    # Limpiar HTML raw
    rst_content = re.sub(r'\.\. raw:: html.*?(?=\n\n|\n\.\.|$)', '', rst_content, flags=re.DOTALL)
    
    # Limpiar TOC
    rst_content = re.sub(r'\.\. toctree::.*?(?=\n\n[^\s]|\Z)', '', rst_content, flags=re.DOTALL)
    
    # Tablas (list-table)
    rst_content = re.sub(
        r'\.\. list-table::.*?\n   :widths: [\d ]+\n   :header-rows: \d+\n\n((?:   \* - .+\n?)+)',
        convert_list_table,
        rst_content,
        flags=re.DOTALL
    )
    
    # Separadores horizontales
    rst_content = re.sub(r'^-{4,}$', '\n---\n', rst_content, flags=re.MULTILINE)
    
    # Limpiar líneas vacías múltiples
    rst_content = re.sub(r'\n{3,}', '\n\n', rst_content)
    
    return rst_content.strip()


def convert_list_table(match):
    """Convierte list-table de RST a tabla Markdown"""
    content = match.group(1)
    rows = content.split('\n   * - ')
    rows = [r for r in rows if r.strip()]
    
    if not rows:
        return ''
    
    # Primera fila es header
    header_parts = rows[0].split('\n     - ')
    md_table = '| ' + ' | '.join(header_parts) + ' |\n'
    md_table += '| ' + ' | '.join(['---'] * len(header_parts)) + ' |\n'
    
    # Resto de filas
    for row in rows[1:]:
        cells = row.split('\n     - ')
        md_table += '| ' + ' | '.join(cells) + ' |\n'
    
    return '\n' + md_table + '\n'


def create_summary(rst_files, output_dir):
    """Crea SUMMARY.md basado en los archivos encontrados"""
    
    # Mapeo de archivos a títulos bonitos
    titles = {
        'index': 'Bienvenido a Aeternum',
        'introduccion': 'Introducción',
        'instalacion': 'Instalación',
        'arquitectura': 'Arquitectura del Sistema',
        'auth_routes': 'Sistema de Autenticación',
        'password_reset': 'Recuperación de Contraseña',
        'usuario': 'Módulo de Usuario',
        'perfil': 'Gestión de Perfil',
        'wishlist': 'Lista de Deseos',
        'catalogo': 'Catálogo de Libros',
        'prestamos': 'Sistema de Préstamos',
        'reviews': 'Reviews y Calificaciones',
        'administracion': 'Panel de Administración',
        'gestion_prestamos': 'Gestión de Préstamos',
        'backend': 'Backend (FastAPI)',
        'frontend': 'Frontend (React + Vite)',
        'api': 'Documentación de la API',
        'seguridad': 'Seguridad',
    }
    
    summary_content = "# Tabla de Contenido\n\n"
    
    # Agrupar por secciones
    sections = {
        '## 🚀 Comenzando': ['index', 'introduccion', 'instalacion', 'arquitectura'],
        '## 🔐 Autenticación': ['auth_routes', 'password_reset'],
        '## 👤 Módulo de Usuarios': ['usuario', 'perfil', 'wishlist'],
        '## 📚 Gestión de Libros': ['catalogo', 'prestamos', 'reviews'],
        '## ⚙️ Administración': ['administracion', 'gestion_prestamos'],
        '## 🔧 Referencia Técnica': ['backend', 'frontend', 'api', 'seguridad'],
    }
    
    for section, files in sections.items():
        summary_content += f"\n{section}\n\n"
        for file_stem in files:
            if any(f.stem == file_stem for f in rst_files):
                title = titles.get(file_stem, file_stem.replace('_', ' ').title())
                summary_content += f"* [{title}]({file_stem}.md)\n"
    
    with open(output_dir / 'SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print("✓ SUMMARY.md creado")


def create_readme(output_dir):
    """Crea README.md de introducción"""
    readme = """# Documentación de Aeternum

Bienvenido a la documentación completa de **Aeternum**, una plataforma moderna de biblioteca virtual.

## 🚀 Inicio Rápido

* [Introducción](introduccion.md) - Conoce el proyecto
* [Instalación](instalacion.md) - Configura tu entorno
* [API Reference](api.md) - Referencia completa de endpoints

## 📚 Contenido

Usa el menú lateral para navegar por todas las secciones de la documentación.

---

**Desarrollado por:** Santiago Tuta  
**Versión:** 1.0.0  
**Licencia:** MIT
"""
    
    with open(output_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("✓ README.md creado")


def convert_file(rst_file, output_dir):
    """Convierte un archivo RST a MD"""
    
    print(f"  Convirtiendo: {rst_file.name}")
    
    # Leer contenido
    try:
        with open(rst_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"    ⚠️  Error al leer {rst_file.name}: {e}")
        return False
    
    # Convertir
    md_content = convert_rst_to_markdown(content)
    
    # Crear nombre de archivo MD
    md_filename = rst_file.stem + '.md'
    output_path = output_dir / md_filename
    
    # Guardar
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"    ✓ Guardado: {md_filename}")
        return True
    except Exception as e:
        print(f"    ⚠️  Error al guardar {md_filename}: {e}")
        return False


def main():
    """Función principal"""
    
    print("\n" + "=" * 70)
    print("📚 CONVERSOR DE DOCUMENTACIÓN RST → GITBOOK MARKDOWN")
    print("=" * 70 + "\n")
    
    # CORREGIDO: Buscar en 'source' en lugar de 'docs'
    source_dir = Path('source')
    output_dir = Path('gitbook_output')
    
    # Verificar que existe la carpeta source
    if not source_dir.exists():
        print(f"❌ ERROR: No se encontró la carpeta '{source_dir}'")
        print("\nAsegúrate de ejecutar el script desde la carpeta raíz del proyecto.")
        print("Estructura esperada:")
        print("  documentacion-proyecto/")
        print("  ├── source/           ← Tus archivos .rst están aquí")
        print("  ├── convert_rst_to_md.py")
        print("  └── ...")
        return
    
    # Crear directorio de salida
    output_dir.mkdir(exist_ok=True)
    
    # Buscar archivos RST
    rst_files = list(source_dir.glob('*.rst'))
    
    if not rst_files:
        print(f"⚠️  No se encontraron archivos .rst en '{source_dir}'")
        print(f"\nContenido de {source_dir}:")
        for item in source_dir.iterdir():
            print(f"  - {item.name}")
        return
    
    print(f"📂 Carpeta origen: {source_dir.absolute()}")
    print(f"📂 Carpeta destino: {output_dir.absolute()}")
    print(f"\n✅ Encontrados {len(rst_files)} archivos RST\n")
    print("=" * 70)
    
    # Convertir archivos
    success_count = 0
    for rst_file in sorted(rst_files):
        if convert_file(rst_file, output_dir):
            success_count += 1
    
    print("=" * 70)
    
    # Crear archivos de configuración
    print("\n📝 Creando archivos de configuración...")
    create_summary(rst_files, output_dir)
    create_readme(output_dir)
    
    # Copiar carpeta _static si existe
    static_dir = source_dir / '_static'
    if static_dir.exists():
        output_static = output_dir / '.gitbook' / 'assets'
        output_static.mkdir(parents=True, exist_ok=True)
        
        try:
            shutil.copytree(static_dir, output_static, dirs_exist_ok=True)
            print(f"✓ Imágenes copiadas a: {output_static}")
        except Exception as e:
            print(f"⚠️  Error al copiar imágenes: {e}")
    else:
        print("ℹ️  No se encontró carpeta _static (imágenes)")
    
    # Resumen final
    print("\n" + "=" * 70)
    print(f"✅ CONVERSIÓN COMPLETADA: {success_count}/{len(rst_files)} archivos")
    print("=" * 70)
    print(f"\n📁 Archivos generados en: {output_dir.absolute()}\n")
    
    print("📝 PRÓXIMOS PASOS:\n")
    print("1. Revisa los archivos en 'gitbook_output/'")
    print("2. Ve a GitBook → https://app.gitbook.com")
    print("3. Crea un nuevo espacio (New Space)")
    print("4. Selecciona 'Import' → 'Upload files'")
    print("5. Arrastra toda la carpeta 'gitbook_output'")
    print("\n💡 TIP: GitBook detectará automáticamente el SUMMARY.md\n")


if __name__ == '__main__':
    main()