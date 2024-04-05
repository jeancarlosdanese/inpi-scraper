#!/bin/bash

# Define o caminho para o diretório do seu projeto
# Atualize isso para o caminho absoluto do seu projeto
PROJECT_DIR="$HOME/inpi-scraper"

# Muda para o diretório do projeto
cd $PROJECT_DIR

# Ativa o ambiente virtual
source ".venv/bin/activate"

# Executa o script Python
python main.py

# Desativa o ambiente virtual
deactivate
