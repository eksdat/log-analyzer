# Analisador de Log de Acessos

Programa de terminal em Python que lê um log de acessos de servidor web e gera um resumo: total de requisições, contagem de erros, horário de pico e os IPs que mais acessaram.

![Python](https://img.shields.io/badge/Python-3-blue)
![Licença](https://img.shields.io/badge/Licença-MIT-green)

## O que faz

Dado um arquivo de log no formato comum (Common Log Format), o programa:

- conta o total de requisições;
- conta os erros (status 4xx e 5xx), separados por código;
- identifica o horário de pico de acessos;
- lista os IPs que mais aparecem.

O ranking de IPs é útil, entre outras coisas, pra notar comportamento fora do normal — por exemplo, um único IP responsável por muito mais acessos que os demais, o que pode indicar uma varredura.

## Exemplo de saída

```
Total de requisicoes: 46
Erros (4xx/5xx): 18
  - 401: 6
  - 404: 9
  - 500: 3
Hora de pico: 10h (19 requisicoes)
Top 3 IPs:
  203.0.113.77 - 13 acessos
  192.168.0.10 - 9 acessos
  198.51.100.23 - 9 acessos
```

## Como funciona

O programa é dividido em três etapas, cada uma numa função:

- `ler_log` — abre o arquivo, recorta cada linha e extrai IP, status e hora, devolvendo uma lista de tuplas.
- `contar` — percorre essa lista e monta três dicionários de contagem (por IP, por status e por hora).
- `exibir_resumo` — calcula os totais, o horário de pico e o ranking, e imprime o relatório.

## Como rodar

1. Tenha o Python 3 instalado.
2. Coloque o arquivo de log (ex.: `access.log`) na mesma pasta do programa.
3. Rode:
   ```bash
   python analisador_log.py
   ```

O repositório inclui um `access.log` de exemplo para teste.

## Estrutura

```
analisador-log/
├── analisador_log.py   programa principal
├── access.log          log de exemplo para teste
└── README.md
```

## Próximos passos

Ideias de evolução já mapeadas: receber o caminho do log como argumento, listar os endpoints mais acessados, sinalizar IPs suspeitos automaticamente, exportar o relatório em JSON e, mais à frente, expor a análise através de uma API.

## Licença

MIT.