import xml.etree.ElementTree as ET


def parse_xml(file_path, process_list):
    """
    Analisa o arquivo XML, procurando por processos específicos na lista fornecida
    e prepara o corpo do e-mail com informações desses processos.
    :param file_path: Caminho para o arquivo XML a ser analisado.
    :param process_list: Lista de números de processo a serem buscados.
    :return: String formatada com informações dos processos para o corpo do e-mail.
    """
    email_body = "Atualizações de Processos INPI:\n\n"
    tree = ET.parse(file_path)
    root = tree.getroot()

    for process_number in process_list:
        process = root.find(f".//processo[@numero='{process_number}']")
        if process is not None:
            email_body += f"Processo Encontrado: {process_number}\n"
            titular = process.find(".//titular")
            despacho = process.find(".//despacho")
            if titular is not None:
                email_body += (
                    f"Titular: {titular.attrib['nome-razao-social']}, {titular.attrib.get('pais')}, {titular.attrib.get('uf', 'N/A')}\n"
                )
            if despacho is not None:
                email_body += f"Despacho: {despacho.attrib['nome']}\n"
            email_body += "\n"  # Espaço entre os processos
        else:
            email_body += f"Processo {process_number} não encontrado.\n\n"

    return email_body
