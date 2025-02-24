import socket
import requests # type: ignore

def scanner_portas(host):
    print(f"Escaneando portas no host: {host}")
    portas_comuns = [22, 80, 443, 8080]
    for porta in portas_comuns:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1) #timeout de um segundo
                resultado = s.connect_ex((host, porta))
                if resultado ==0:
                    print(f"Porta {porta} está aberta!")
                else:
                    print(f"Porta {porta} está fechada.") 
        except Exception as e:
            print(f"Erro ao verificar porta {porta}: {e}")

def verificar_headers_http(url):
    print(f"\nVerificando headers HTTP em {url}")
    try: 
        resposta = requests.get(url, timeout=5)
        headers = resposta.headers
        if 'X-Content-Type-Options' in headers:
            print(f"Header X-Content-Type-Options presente.")
        else:
            print(f"Header X-Content-Type-Options ausente")
    except Exception as e: 
        print(f"Erro ao verificar URL: {e}")

if __name__ == "__main__":
    host = input("Digite o endereço IP ou domínio para escanear: ")
    scanner_portas(host)

    url = input("\nDigite a URL para verificar headers HTTP (ex: http://site.com): ")
    verificar_headers_http(url)