import os
import boto3
from botocore.exceptions import ClientError


def send_email_via_ses(from_addresses, to_addresses, subject, body):
    # Cliente SES no us-east-1 por padrão, ajuste conforme necessário
    region_name = os.getenv("AWS_REGION")
    ses_client = boto3.client("ses", region_name=region_name)

    try:
        response = ses_client.send_email(
            Source=from_addresses,  # O endereço de e-mail VERIFICADO do remetente
            Destination={"ToAddresses": to_addresses},  # Lista de endereços de e-mail dos destinatários
            Message={"Subject": {"Data": subject, "Charset": "UTF-8"}, "Body": {"Text": {"Data": body, "Charset": "UTF-8"}}},
        )
        print("E-mail enviado com sucesso! Message ID:", response["MessageId"])
    except ClientError as e:
        print("Não foi possível enviar o e-mail. Error:", e.response["Error"]["Message"])


# Uso do exemplo
if __name__ == "__main__":
    from_addresses = ["origem@domain.com.br"]
    to_addresses = ["destinatario@domain.com.br"]
    subject = "Alerta de Processo INPI"
    body = "Este é um teste de envio de e-mail utilizando o Amazon SES para alertas de processo."
    send_email_via_ses(from_addresses, to_addresses, subject, body)
