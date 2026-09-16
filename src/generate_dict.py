
#### 4. `src/generate_dict.py` (O motor do projeto)
```python
import os
import sys

def generate_dictionary(lang_code):
    print(f"🚀 Iniciando geração do dicionário para: {lang_code}")
    
    data_dir = f"data/{lang_code}"
    output_dic = f"pt_BR_cientifico_ia.dic" if lang_code == "pt-BR" else f"en_US_scientific_ai.dic"
    
    # Se o arquivo de saída for en-US, ajustamos o nome (simplificação para o script)
    if lang_code == "en-US":
        output_dic = "en_US_scientific_ai.dic"

    palavras = set()

    # 1. Ler todos os arquivos .txt na pasta de dados do idioma
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            if filename.endswith(".txt"):
                filepath = os.path.join(data_dir, filename)
                print(f"  📖 Lendo: {filename}")
                with open(filepath, 'r', encoding='utf-8') as f:
                    for linha in f:
                        palavra = linha.strip().lower()
                        # Filtra linhas vazias. Mantém hífens e apóstrofos.
                        if palavra and (palavra.isalpha() or '-' in palavra or "'" in palavra):
                            palavras.add(palavra)
    else:
        print(f"⚠️ Aviso: Pasta {data_dir} não encontrada.")

    # 2. Limpeza e ordenação alfabética
    palavras_finais = sorted(list(palavras))

    # 3. Escrever o arquivo .dic com o contador na PRIMEIRA linha (Regra do Hunspell)
    with open(output_dic, 'w', encoding='utf-8') as f:
        f.write(f"{len(palavras_finais)}\n")
        for p in palavras_finais:
            f.write(f"{p}\n")

    print(f"✅ Sucesso! '{output_dic}' gerado com {len(palavras_finais)} termos únicos.")
    print(f"💡 Próximo passo: Copie o arquivo .aff original do LibreOffice para a mesma pasta e renomeie para corresponder ao .dic (ex: {output_dic.replace('.dic', '.aff')})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        lang = sys.argv[1]
        generate_dictionary(lang)
    else:
        print("Uso: python generate_dict.py <pt-BR|en-US>")