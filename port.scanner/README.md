# Scanner de Portas e Verificador de Headers HTTP

Este projeto inclui duas ferramentas básicas de segurança:

1. **Scanner de Portas**: Um script simples que escaneia portas comuns (22, 80, 443, 8080) em um host fornecido (IP ou domínio) para verificar se estão abertas ou fechadas.
2. **Verificador de Header HTTP**: Uma ferramenta que verifica a presença do header `X-Content-Type-Options` em uma URL fornecida.

## Funcionalidades
- **Scanner de Portas**: Verifica se portas específicas estão abertas no host fornecido.
- **Verificação de Header HTTP**: Garante a presença de headers de segurança, especificamente o `X-Content-Type-Options`, para melhorar a segurança e prevenir sniffing de tipos MIME.

## Requisitos
- Python 3.x
- Biblioteca `requests` (para verificação de headers HTTP)

Você pode instalar a biblioteca `requests` usando o pip:
```bash
pip install requests


# Port Scanner and HTTP Header Checker

This project includes two basic security tools:

1. **Port Scanner**: A simple script that scans common ports (22,80,443, 8080) on a given host (IP or domain) to check if they are open or closed.
2. **HTTP Header Checker**: A toll that checks for the presence of the `X-Contetn-Type-Options` HTTP header on a given URL.


## Features
**Port Scanning**: Verifies if specific ports are on the provided host.
**HTTP Header Ckecking**: Ensures the presence of security headers, specifically `X-Content-Type-Options` to improve security by preventing MIME type sniffing.

## Requirements
- Python 3.x
- `requests` library (for HTTP header checking)

You can install the `requests`using pip:
```bash
pip install resquests



