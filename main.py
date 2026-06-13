# le o arquivo de log e retorna uma lista (ip, status, hora)
def ler_log(caminho):
    entradas = []
    with open(caminho) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            # divide a linha em partes usando espaco como separador
            partes = linha.split()

            ip = partes[0]       # primeiro campo e o IP
            status = partes[-2]  # penultimo campo e o status code

            # campo 3 tem formato [13/Jun/2026:10:00:01, split por ":" pega a hora
            campo_data = partes[3]
            hora = campo_data.split(":")[1]

            entradas.append((ip, status, hora))
    return entradas


# recebe a lista de entradas e conta ocorrencias de ip, status e hora
def contar(entradas):
    contagem_ips = {}
    contagem_status = {}
    contagem_horas = {}

    for ip, status, hora in entradas:
        # get(chave, 0) evita KeyError quando a chave ainda nao existe
        contagem_ips[ip] = contagem_ips.get(ip, 0) + 1
        contagem_status[status] = contagem_status.get(status, 0) + 1
        contagem_horas[hora] = contagem_horas.get(hora, 0) + 1

    return contagem_ips, contagem_status, contagem_horas


# imprime o relatorio final com totais, erros, hora de pico e top 3 IPs
def exibir_resumo(entradas, contagem_ips, contagem_status, contagem_horas):
    total = len(entradas)

    # soma os valores de todos os status >= 400 (erros de cliente e servidor)
    erros = sum(v for k, v in contagem_status.items() if int(k) >= 400)

    # max com key=dicionario.get devolve a chave com o maior valor
    hora_pico = max(contagem_horas, key=contagem_horas.get)

    # sorted com reverse=True ordena do maior pro menor
    ranking_ips = sorted(contagem_ips.items(), key=lambda p: p[1], reverse=True)

    print(f"Total de requisicoes: {total}")
    print(f"Erros (4xx/5xx): {erros}")

    # percorre so os status de erro em ordem numerica
    for codigo in sorted(k for k in contagem_status if int(k) >= 400):
        print(f"  - {codigo}: {contagem_status[codigo]}")

    print(f"Hora de pico: {hora_pico}h ({contagem_horas[hora_pico]} requisicoes)")
    print("Top 3 IPs:")

    # [:3] pega so os tres primeiros itens da lista ordenada
    for ip, qtd in ranking_ips[:3]:
        print(f"  {ip} - {qtd} acessos")


def main():
    entradas = ler_log("access.log")
    contagem_ips, contagem_status, contagem_horas = contar(entradas)
    exibir_resumo(entradas, contagem_ips, contagem_status, contagem_horas)

if __name__ == "__main__":
    main()