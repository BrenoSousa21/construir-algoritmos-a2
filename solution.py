
import datetime
import requests


def cotar():
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)

        data = dia.strftime("%m-%d-%Y")
        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            f"CotacaoDolarDia(dataCotacao='{data}')"
            "?$format=json"
        )

        resposta = requests.get(url)
        dados = resposta.json()

        if dados["value"]:
            cotacao = dados["value"][0]["cotacaoCompra"]
            print(f"{dia}: R$ {cotacao:.4f}")
        else:
            print(f"{dia}: Sem cotação disponível")


if __name__ == "__main__":
    cotar()
