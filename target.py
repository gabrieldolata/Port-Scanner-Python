import socket
import sys
import psycopg2
from datetime import datetime

target = input("Digite o IP ou domínio para verificação: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[Erro] Não foi possível resolver o nome do host.")
    sys.exit()

print("-" * 60)
print(f"Escaneando o ip: {target_ip}")
print(f"Início do scan: {str(datetime.now())}")
print("-" * 60)

portas_comuns = [21, 22, 53, 80, 135, 139, 443, 445, 3306, 5432, 8000, 8080]

try:
    for porta in portas_comuns:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(2.0)
        
        resultado = s.connect_ex((target_ip, porta))
        
        if resultado == 0:
            print(f"Porta {porta}: ABERTA ✔️")
        else:
            print(f"Porta {porta}: Fechada ❌")
            
        s.close()

except KeyboardInterrupt:
    print("\n[Aviso] Scan interrompido pelo usuário.")
    sys.exit()

except socket.error:
    print("\n[Erro] Não foi possível conectar ao servidor.")
    sys.exit()

print("-" * 60)
print("Verificação finalizada com sucesso!")