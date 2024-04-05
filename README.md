# INPI Scraper

## Descrição

Este projeto é um scraper automatizado para monitorar e alertar sobre atualizações de processos específicos do INPI (Instituto Nacional da Propriedade Industrial). Ele automatiza a tarefa de verificar novos registros ou atualizações em registros existentes, e envia alertas via e-mail para os interessados.

## Pré-Requisitos

- Python 3.8+
- Pip (Gerenciador de pacotes Python)
- Ambiente virtual Python (recomendado)
- Conta AWS configurada com Amazon SES para envio de e-mails

## Configuração

1. **Clone o repositório para o seu ambiente local:**

   ```bash
   git clone https://github.com/seu-usuario/inpi-scraper.git
   ```

2. **Navegue até o diretório do projeto e crie um ambiente virtual Python:**

   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual:**

   - No Linux/Mac:

   ```bash
   source .venv/bin/activate
   ```

   - No Windows:

   ```bash
   .venv\Scripts\activate
   ```

4. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Copie o arquivo .env.example para .env e ajuste as variáveis de ambiente conforme sua configuração:**

   ```bash
   cp .env.example .env
   ```

6. **Certifique-se de verificar seu e-mail de origem e destinatário no Amazon SES.**

## Execução

Execute o script principal para iniciar o monitoramento e envio de alertas:

```bash
./run_inpi_scraper.sh
```

## Agendamento Automático com Crontab (Linux)

Para agendar a execução automática do script:

1. **Abra o crontab com:**

   ```bash
   crontab -e
   ```

2. **Adicione uma nova linha para agendar sua tarefa, por exemplo, para executar todos os dias às 6 da manhã:**

   ```bash
   0 6 * * * /caminho/para/o/projeto/run_inpi_scraper.sh
   ```

## Instituições Relevantes

- **[INPI (Instituto Nacional da Propriedade Industrial)](https://www.gov.br/inpi/pt-br)**: Órgão responsável pela concessão e registro de marcas, patentes e outros direitos de propriedade intelectual no Brasil.

- **[WIPO (World Intellectual Property Organization)](https://www.wipo.int/portal/en/index.html)**: Organização global dedicada a proteger direitos de propriedade intelectual e incentivar a inovação.
