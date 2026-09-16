#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Dictionary Script for Scientific and AI LibreOffice Extension

This script reads term lists from data/ directories and taxonomy .dic files,
combines them, and generates Hunspell-compatible .dic files with proper
word counts on the first line.

Usage:
    python src/build_dict.py
"""

import os
from pathlib import Path


def read_txt_files(directory: Path) -> set:
    """Read all .txt files in a directory and extract words/terms."""
    words = set()
    if not directory.exists():
        print(f"⚠️  Directory {directory} does not exist. Skipping...")
        return words
    
    for txt_file in directory.glob("*.txt"):
        print(f"📖 Reading {txt_file.name}...")
        with open(txt_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                if word:  # Ignore empty lines
                    words.add(word)
    return words


def read_dic_file(filepath: Path) -> set:
    """Read a Hunspell .dic file, skipping the first line (word count)."""
    words = set()
    if not filepath.exists():
        print(f"⚠️  File {filepath} does not exist. Skipping...")
        return words
    
    print(f"📖 Reading taxonomy dictionary {filepath.name}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Skip first line (it's the word count)
        for line in lines[1:]:
            # Extract only the word part (before any slash or space)
            word = line.strip().lower()
            if '/' in word:
                word = word.split('/')[0]
            word = word.split(' ')[0]  # Take only first word if space exists
            if word:
                words.add(word)
    return words


def write_dic_file(filepath: Path, words: set):
    """Write words to a Hunspell .dic file with count on first line."""
    sorted_words = sorted(words)
    word_count = len(sorted_words)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"{word_count}\n")
        for word in sorted_words:
            f.write(f"{word}\n")
    
    return word_count


def main():
    base_dir = Path(__file__).parent.parent
    input_taxonomy_dir = base_dir / "input" / "taxonomy"
    data_ptbr_dir = base_dir / "data" / "pt-BR"
    data_enus_dir = base_dir / "data" / "en-US"
    
    print("=" * 60)
    print("🔬 Building Scientific and AI Dictionary for LibreOffice")
    print("=" * 60)
    print()
    
    # Process pt-BR dictionary
    print("🇧🇷 Processing pt-BR dictionary...")
    print("-" * 40)
    ptbr_words = set()
    
    # Read from data/pt-BR/*.txt
    ptbr_words.update(read_txt_files(data_ptbr_dir))
    
    # Read from input/taxonomy/*.dic (if exists)
    for dic_file in input_taxonomy_dir.glob("*.dic"):
        ptbr_words.update(read_dic_file(dic_file))
    
    if ptbr_words:
        output_ptbr = base_dir / "pt_BR_cientifico_ia.dic"
        count_ptbr = write_dic_file(output_ptbr, ptbr_words)
        print(f"✅ Generated {output_ptbr.name} with {count_ptbr} terms")
    else:
        print("⚠️  No pt-BR terms found. File not generated.")
    
    print()
    
    # Process en-US dictionary
    print("🇺🇸 Processing en-US dictionary...")
    print("-" * 40)
    enus_words = set()
    
    # Read from data/en-US/*.txt
    enus_words.update(read_txt_files(data_enus_dir))
    
    # Read from input/taxonomy/*.dic (if exists)
    for dic_file in input_taxonomy_dir.glob("*.dic"):
        enus_words.update(read_dic_file(dic_file))
    
    if enus_words:
        output_enus = base_dir / "en_US_scientific_ai.dic"
        count_enus = write_dic_file(output_enus, enus_words)
        print(f"✅ Generated {output_enus.name} with {count_enus} terms")
    else:
        print("⚠️  No en-US terms found. File not generated.")
    
    print()
    print("=" * 60)
    print("📋 NEXT STEPS - IMPORTANT INSTRUCTIONS:")
    print("=" * 60)
    print()
    print("1️⃣  COPY THE AFFIX FILE FROM LIBREOFFICE:")
    print("   You need to copy the original .aff file from your LibreOffice installation")
    print("   and rename it to match the generated .dic files.")
    print()
    print("   For pt-BR:")
    print("   - Locate: pt_BR.aff (usually in /usr/share/hunspell/ or C:\\Program Files\\LibreOffice\\share\\hunspell\\)")
    print("   - Copy to this directory and rename to: pt_BR_cientifico_ia.aff")
    print()
    print("   For en-US:")
    print("   - Locate: en_US.aff (same locations as above)")
    print("   - Copy to this directory and rename to: en_US_scientific_ai.aff")
    print()
    print("2️⃣  CREATE THE EXTENSION (.oxt):")
    print("   Select these files and compress them into a ZIP:")
    print("   - pt_BR_cientifico_ia.dic")
    print("   - pt_BR_cientifico_ia.aff (the copied/renamed one)")
    print("   - en_US_scientific_ai.dic")
    print("   - en_US_scientific_ai.aff (the copied/renamed one)")
    print("   - templates/dictionaries.xcu")
    print("   - templates/description.xml")
    print()
    print("   Then rename the .zip file to .oxt")
    print()
    print("3️⃣  INSTALL IN LIBREOFFICE:")
    print("   - Open LibreOffice")
    print("   - Go to Tools > Extension Manager")
    print("   - Click 'Add' and select your .oxt file")
    print("   - Restart LibreOffice")
    print()
    print("=" * 60)
    print("✨ Build complete! Your dictionaries are ready.")
    print("=" * 60)


if __name__ == "__main__":
    main()
