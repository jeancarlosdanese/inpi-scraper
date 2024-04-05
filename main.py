import os
from dotenv import load_dotenv
from src.scraper import find_latest_edition_url, download_zip
from src.parser import parse_xml
from src.sendmail import send_email_via_ses

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()


def main():
    # Diretório onde o arquivo ZIP será salvo e extraído
    download_dir = "./data/downloaded/"

    # Certifique-se de que o diretório existe
    os.makedirs(download_dir, exist_ok=True)

    # Lista de números de processo a serem buscados
    process_list = os.getenv("PROCESSOS").split(",")

    # Etapa 1: Encontre a URL do arquivo ZIP mais recente e o nome esperado do arquivo XML
    print("Procurando pela URL do arquivo ZIP mais recente e nome do arquivo XML...")
    zip_url, xml_file_name = find_latest_edition_url()
    if not zip_url:
        print("Não foi possível encontrar o arquivo ZIP.")
        return

    # Etapa 2: Baixe e extraia o arquivo ZIP
    print(f"Baixando e extraindo o arquivo ZIP de {zip_url}...")
    download_zip(zip_url, download_dir)

    # O caminho completo para o arquivo XML extraído
    xml_file_path = os.path.join(download_dir, xml_file_name)

    # Etapa 3: Analise o arquivo XML para encontrar os processos especificados
    print(f"Analisando o arquivo XML em {xml_file_path}...")
    email_body = parse_xml(xml_file_path, process_list)

    # Enviar e-mail
    from_addresses = os.getenv("EMAIL_ORIGEM")
    to_addresses = [os.getenv("EMAIL_DESTINATARIO")]
    subject = "Atualização de Processos INPI"
    send_email_via_ses(from_addresses, to_addresses, subject, email_body)


if __name__ == "__main__":
    main()
