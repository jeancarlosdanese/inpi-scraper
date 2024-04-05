import requests
from bs4 import BeautifulSoup
import os
import zipfile
import io

# Configuração inicial
URL_BASE = "https://revistas.inpi.gov.br/rpi/"


def download_zip(url, path_to_save):
    """
    Faz o download do arquivo ZIP e salva localmente.
    """
    response = requests.get(url)
    if response.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(path_to_save)
    else:
        print(f"Erro ao baixar o arquivo ZIP: {response.status_code}")


def find_latest_edition_url():
    """
    Encontra a URL do último arquivo ZIP da SEÇÃO V MARCAS na página do INPI.
    """
    response = requests.get(URL_BASE)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # A estrutura do site indica que a URL desejada está na tabela, especificamente na coluna SEÇÃO V MARCAS
        # Vamos encontrar a primeira ocorrência da URL do arquivo ZIP na SEÇÃO V MARCAS
        link = soup.find("a", href=True, text="XML")
        if link:
            zip_url = link["href"]
            print(f"URL do arquivo ZIP encontrado: {zip_url}")

            # Supondo que você possa derivar o nome do arquivo XML do nome do arquivo ZIP ou de alguma convenção
            # Exemplo: se o nome do ZIP é 'RM2778.zip', o XML pode ser 'RM2778.xml'
            # Você precisará ajustar esta lógica com base na estrutura real dos nomes dos arquivos.
            xml_file_name = zip_url.split("/")[-1].replace(".zip", ".xml")

            return zip_url, xml_file_name
        else:
            print("Arquivo ZIP da SEÇÃO V MARCAS não encontrado.")
            return None
    else:
        print(f"Erro ao acessar {URL_BASE}: {response.status_code}")
        return None


def main():
    path_to_save = "./data/downloaded/"
    os.makedirs(path_to_save, exist_ok=True)

    zip_url = find_latest_edition_url()
    if zip_url:
        print(f"Baixando arquivo de {zip_url}")
        download_zip(zip_url, path_to_save)
        print(f"Arquivo baixado e extraído em {path_to_save}")
    else:
        print("Não foi possível encontrar o arquivo ZIP.")
