# 📚 Dicionário Científico e de IA para LibreOffice

## 🔬 Scientific and AI Dictionary for LibreOffice

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LibreOffice](https://img.shields.io/badge/LibreOffice-4.0+-blue.svg)](https://www.libreoffice.org/)

---

## ❌ O Problema

Se você já tentou escrever documentos técnicos, científicos ou sobre Inteligência Artificial no LibreOffice, provavelmente enfrentou este problema:

- **Termos técnicos são marcados como erros**: Palavras como "backpropagation", "embedding", "fine-tuning", "transformer" aparecem sublinhadas em vermelho.
- **A "gambiarra" do Latim**: Muitos dicionários científicos existentes obrigam você a mudar o idioma do texto para "Latim (la)" para que os termos sejam aceitos.
- **Consequência**: Ao mudar para Latim, **você perde toda a correção gramatical** do português ou inglês, incluindo concordância, pontuação e estilo.

Isso é inaceitável para quem precisa produzir documentos técnicos profissionais.

---

## ✅ A Solução

Esta extensão resolve o problema de forma elegante:

1. **Complementa os dicionários nativos**: Em vez de substituir o dicionário pt-BR ou en-US, ele **adiciona** termos técnicos como complemento.
2. **Mantém o idioma correto**: Seu documento continua em "Português (Brasil)" ou "English (US)", preservando toda a correção gramatical.
3. **Reconhecimento simultâneo**: O LibreOffice usa o dicionário padrão **E** o dicionário científico ao mesmo tempo.
4. **Focado em IA e Ciência de Dados**: Inclui centenas de termos de machine learning, deep learning, NLP e áreas relacionadas.

---

## 📦 Como Usar (Passo a Passo)

### Pré-requisitos
- Python 3.6+ instalado
- LibreOffice 4.0 ou superior
- Arquivos do "Taxonomy Dictionary" (.dic e .aff) que você já baixou

---

### Passo 1: Coloque os Arquivos do Taxonomy Dictionary

Copie os arquivos `.dic` e `.aff` que você baixou do "Taxonomy Dictionary" para a pasta `input/taxonomy/`:

```
cientific-dictionary/
├── input/
│   └── taxonomy/
│       ├── seu_arquivo.dic    <-- COLE AQUI
│       └── seu_arquivo.aff    <-- COLE AQUI
├── data/
├── src/
└── templates/
```

> **Nota**: O script vai ler automaticamente qualquer arquivo `.dic` nesta pasta.

---

### Passo 2: Execute o Script de Build

No terminal, navegue até a raiz do projeto e execute:

```bash
python src/build_dict.py
```

O script irá:
- Ler todos os termos de `data/pt-BR/*.txt` e `data/en-US/*.txt`
- Ler os arquivos `.dic` da pasta `input/taxonomy/`
- Combinar tudo, remover duplicatas e ordenar alfabeticamente
- Gerar `pt_BR_cientifico_ia.dic` e `en_US_scientific_ai.dic` na raiz

**Saída esperada:**
```
============================================================
🔬 Building Scientific and AI Dictionary for LibreOffice
============================================================

🇧🇷 Processing pt-BR dictionary...
----------------------------------------
📖 Reading ai_ml_terms.txt...
✅ Generated pt_BR_cientifico_ia.dic with 68 terms

🇺🇸 Processing en-US dictionary...
----------------------------------------
📖 Reading ai_ml_terms.txt...
✅ Generated en_US_scientific_ai.dic with 76 terms

============================================================
📋 NEXT STEPS - IMPORTANT INSTRUCTIONS:
============================================================
...
```

---

### Passo 3: Copie e Renomeie os Arquivos .aff do LibreOffice

Você precisa dos arquivos de afixo originais do LibreOffice. Eles contêm as regras de flexão para cada idioma.

#### No Linux:
```bash
# Para pt-BR
sudo cp /usr/share/hunspell/pt_BR.aff ./pt_BR_cientifico_ia.aff

# Para en-US
sudo cp /usr/share/hunspell/en_US.aff ./en_US_scientific_ai.aff
```

#### No Windows:
```
C:\Program Files\LibreOffice\share\hunspell\pt_BR.aff  →  copiar para  pt_BR_cientifico_ia.aff
C:\Program Files\LibreOffice\share\hunspell\en_US.aff  →  copiar para  en_US_scientific_ai.aff
```

#### No macOS:
```bash
# Dentro do aplicativo LibreOffice
/Applications/LibreOffice.app/Contents/Resources/hunspell/pt_BR.aff  →  pt_BR_cientifico_ia.aff
/Applications/LibreOffice.app/Contents/Resources/hunspell/en_US.aff  →  en_US_scientific_ai.aff
```

---

### Passo 4: Crie a Extensão (.oxt)

Selecione os seguintes arquivos na raiz do projeto:

- `pt_BR_cientifico_ia.dic`
- `pt_BR_cientifico_ia.aff`
- `en_US_scientific_ai.dic`
- `en_US_scientific_ai.aff`
- `templates/dictionaries.xcu`
- `templates/description.xml`

**No Linux/macOS:**
```bash
zip -r scientific_dictionary.oxt \
    pt_BR_cientifico_ia.dic \
    pt_BR_cientifico_ia.aff \
    en_US_scientific_ai.dic \
    en_US_scientific_ai.aff \
    templates/dictionaries.xcu \
    templates/description.xml
```

**No Windows:**
1. Selecione os 6 arquivos listados acima
2. Clique com o botão direito → "Enviar para" → "Pasta compactada (ZIP)"
3. Renomeie o arquivo de `.zip` para `.oxt`

---

### Passo 5: Instale no LibreOffice

1. Abra o LibreOffice (Writer, Calc, ou qualquer componente)
2. Vá em **Ferramentas** → **Gerenciador de Extensões...**
3. Clique em **Adicionar...**
4. Selecione o arquivo `scientific_dictionary.oxt`
5. Aceite os termos de licença
6. **Reinicie o LibreOffice**

---

### Passo 6: Verifique a Instalação

Após reiniciar:

1. Abra um documento no Writer
2. Digite termos técnicos como "backpropagation", "fine-tuning", "embeddings"
3. Certifique-se de que o idioma do parágrafo está definido como **Português (Brasil)** ou **English (US)**
4. Os termos **não devem aparecer sublinhados em vermelho** ✅

---

## 📁 Estrutura do Projeto

```
cientific-dictionary/
├── input/
│   └── taxonomy/          # Cole aqui seus arquivos .dic e .aff baixados
├── data/
│   ├── pt-BR/
│   │   └── ai_ml_terms.txt    # Termos em português e inglês misturados
│   └── en-US/
│       └── ai_ml_terms.txt    # Termos exclusivamente em inglês
├── src/
│   └── build_dict.py      # Script principal de build
├── templates/
│   ├── dictionaries.xcu   # Configuração de registro dos dicionários
│   └── description.xml    # Metadados da extensão
├── README.md              # Este arquivo
├── .gitignore             # Ignora arquivos gerados
├── pt_BR_cientifico_ia.dic    # Gerado pelo script
├── pt_BR_cientifico_ia.aff    # Copiado manualmente do LibreOffice
├── en_US_scientific_ai.dic    # Gerado pelo script
└── en_US_scientific_ai.aff    # Copiado manualmente do LibreOffice
```

---

## 📝 Termos Incluídos

### Português (pt-BR)
- inteligência artificial, aprendizado de máquina, machine learning
- deep learning, rede neural, backpropagation
- dataset, embedding, epoch, fine-tuning
- transformer, overfitting, underfitting, bias, viés
- prompt, llm, modelo de linguagem, pesos, dropout
- E muitos mais... (68 termos na versão atual)

### English (en-US)
- artificial intelligence, machine learning, deep learning
- neural network, backpropagation, dataset, embedding
- epoch, fine-tuning, hallucination, inference
- transformer, overfitting, underfitting, bias, biases
- prompt, llm, large language model, weights, dropout
- And many more... (76 terms in current version)

---

## 🔧 Personalização

### Adicionar Novos Termos

Para adicionar mais termos ao dicionário:

1. Edite `data/pt-BR/ai_ml_terms.txt` ou `data/en-US/ai_ml_terms.txt`
2. Adicione uma palavra/frase por linha
3. Execute `python src/build_dict.py` novamente
4. Recrie a extensão .oxt (Passo 4)
5. Reinstale no LibreOffice

### Criar Listas de Termos Adicionais

Você pode criar novos arquivos `.txt` nas pastas `data/pt-BR/` ou `data/en-US/`:

```
data/
├── pt-BR/
│   ├── ai_ml_terms.txt
│   ├── biologia_terms.txt    # Novo arquivo que você criou
│   └── fisica_terms.txt      # Novo arquivo que você criou
└── en-US/
    ├── ai_ml_terms.txt
    └── chemistry_terms.txt   # Novo arquivo que você criou
```

O script `build_dict.py` lê **todos** os arquivos `.txt` nessas pastas automaticamente.

---

## ⚠️ Limitações Conhecidas

1. **Termos compostos com espaços**: Alguns termos como "machine learning" podem não ser reconhecidos como uma única unidade em todas as situações, dependendo de como o Hunspell processa frases.
2. **Flexões**: Esta versão não adiciona regras de flexão personalizadas. Termos são adicionados como palavras estáticas.
3. **Atualizações**: Se o LibreOffice atualizar seus dicionários base, você pode precisar recopiar os arquivos `.aff`.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do repositório
2. Adicionar novos termos em `data/pt-BR/` ou `data/en-US/`
3. Reportar issues para termos que ainda faltam
4. Sugerir melhorias no script de build

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- Projeto **Hunspell**: Pela engine de verificação ortográfica
- **The Document Foundation**: Pelo LibreOffice e suporte a extensões
- Comunidade de **Ciência de Dados e IA**: Pelos termos que tornam este dicionário possível

---

## 📞 Suporte

Se você encontrar problemas:

1. Verifique se os arquivos `.aff` foram copiados corretamente
2. Certifique-se de que o idioma do parágrafo está definido como pt-BR ou en-US
3. Reinicie o LibreOffice após instalar a extensão
4. Abra uma issue neste repositório

---

**Desenvolvido com ❤️ para a comunidade científica e de IA**
