# 📚 Dicionário Científico e de IA para LibreOffice

Este projeto fornece dicionários Hunspell estendidos para o LibreOffice (e outras ferramentas compatíveis, como Firefox e Thunderbird), adicionando vocabulário científico, médico e de Inteligência Artificial/Aprendizado de Máquina aos idiomas **Português (Brasil)** e **Inglês (EUA)**.

## 🚨 O Problema
O verificador ortográfico padrão do LibreOffice falha constantemente em termos técnicos. Muitas extensões existentes tentam resolver isso mapeando os termos para a língua "Latim", o que obriga o usuário a mudar o idioma do texto manualmente, quebrando a correção gramatical do idioma principal. Isso é contraproducente.

## ✅ A Solução
Este projeto cria extensões (`.oxt`) que **injetam** os termos técnicos como complementos válidos do idioma `pt-BR` (ou `en-US`). O LibreOffice verifica o dicionário padrão E o dicionário científico simultaneamente, sem que você precise alterar o idioma do seu documento.

## 🚀 Instalação Rápida

1. Vá até a aba [Releases](https://github.com/hugodepaula/cientific-dictionary/releases) deste repositório.
2. Baixe a extensão mais recente (`.oxt`) para o seu idioma (ex: `pt-BR-scientific-ai.oxt`).
3. No LibreOffice, abra **Ferramentas > Gerenciador de Extensões**.
4. Clique em **Adicionar** e selecione o arquivo `.oxt` baixado.
5. Reinicie o LibreOffice.
6. Certifique-se de que o idioma do texto está definido como "Português (Brasil)" ou "Inglês (EUA)". Os termos científicos não serão mais marcados como erro.

## 🛠️ Como Gerar os Dicionários Localmente

Se você deseja personalizar os termos ou gerar os arquivos do zero:

1. Certifique-se de ter o Python 3 instalado.
2. Coloque seus arquivos de termos brutos (ex: `decs_pt.txt`) na pasta `data/pt-BR/`.
3. Execute o script de geração:
   ```bash
   python src/generate_dict.py pt-BR
   python src/generate_dict.py en-US