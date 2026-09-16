#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal de construção da extensão.
Lê termos locais + taxonomia, gera .dic e empacota .oxt.
"""
import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
INPUT_TAX = ROOT / "input" / "taxonomy"
DATA_PT = ROOT / "data" / "pt-BR"
DATA_EN = ROOT / "data" / "en-US"
OUTPUT = ROOT / "output"
TEMPLATES = ROOT / "templates"

def load_words_from_txt(folder):
    words = set()
    if not folder.exists(): return words
    for f in folder.glob("*.txt"):
        with open(f, "r", encoding="utf-8") as file:
            for line in file:
                w = line.strip().lower()
                if w and not w.startswith("#"):
                    words.add(w)
    return words

def load_words_from_dic(folder):
    words = set()
    if not folder.exists(): return words
    for f in folder.glob("*.dic"):
        with open(f, "r", encoding="utf-8", errors="ignore") as file:
            for i, line in enumerate(file):
                line = line.strip()
                if not line:
                    continue
                # Pula primeira linha (contador) se for número
                if i == 0 and line.isdigit():
                    continue
                if "/" in line:
                    line = line.split("/")[0].strip()
                if line.startswith(("#", "-", "http", "Version", "License", "Check out")):
                    continue
                w = line.lower()
                if w:
                    words.add(w)
    return words

def build_lang(lang_code, data_folder, output_name):
    print(f"Processando {lang_code}...")
    words = set()
    
    # 1. Termos locais (IA + Biologia)
    words.update(load_words_from_txt(data_folder))
    
    # 2. Taxonomia (se existir)
    words.update(load_words_from_dic(INPUT_TAX))
    
    sorted_words = sorted(words)
    
    # Salvar .dic
    dic_path = OUTPUT / f"{output_name}.dic"
    with open(dic_path, "w", encoding="utf-8") as f:
        f.write(f"{len(sorted_words)}\n")
        for w in sorted_words:
            f.write(f"{w}\n")
    print(f"  -> {len(sorted_words)} palavras em {dic_path}")
    
    # Copiar .aff (procura em data_folder, input ou cria fallback básico)
    source_aff = data_folder / f"{lang_code}.aff"
    if not source_aff.exists():
        source_aff = ROOT / "input" / f"{lang_code}.aff"
    if not source_aff.exists():
        affs = list(ROOT.glob("input/*.aff")) + list(data_folder.glob("*.aff"))
        source_aff = affs[0] if affs else None
    
    dest_aff = OUTPUT / f"{output_name}.aff"
    if source_aff and source_aff.exists():
        shutil.copy(source_aff, dest_aff)
        print(f"  -> Copiado {source_aff.name} para {dest_aff}")
    else:
        with open(dest_aff, "w", encoding="utf-8") as aff_f:
            aff_f.write("SET UTF-8\n")
        print(f"  -> AVISO: Nenhum .aff encontrado para {lang_code}. Gerado .aff padrão em {dest_aff}")

def create_oxt():
    print("Criando pacote .oxt...")
    oxt_path = ROOT / "Dicionario_Cientifico_Abrangente.oxt"
    
    with zipfile.ZipFile(oxt_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona arquivos gerados (.dic e .aff)
        for f in OUTPUT.glob("*"):
            if f.is_file():
                zipf.write(f, f.name)
        
        # Adiciona templates e manifesto
        if (TEMPLATES / "dictionaries.xcu").exists():
            zipf.write(TEMPLATES / "dictionaries.xcu", "dictionaries.xcu")
        if (TEMPLATES / "description.xml").exists():
            zipf.write(TEMPLATES / "description.xml", "description.xml")
        manifest_file = TEMPLATES / "META-INF" / "manifest.xml"
        if manifest_file.exists():
            zipf.write(manifest_file, "META-INF/manifest.xml")
        
    print(f"Extensão criada: {oxt_path}")

if __name__ == "__main__":
    OUTPUT.mkdir(exist_ok=True)
    
    build_lang("pt_BR", DATA_PT, "pt_BR_scientific")
    build_lang("en_US", DATA_EN, "en_US_scientific")
    
    create_oxt()
    print("\n✅ Build concluído com sucesso!")
