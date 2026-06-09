Projeto desenvolvido em Python focado em segurança de redes, auditoria de infraestrutura e integração com bancos de dados. 
O script realiza a varredura das portas de rede mais comuns (IP ou domínio), para identificar serviços ativos. 
Também possui estrutura para persistência de dados em ambientes PostgreSQL.
Converte nomes de domínio (ex: google.com) em endereços IP de forma automatizada usando a biblioteca nativa `socket`.
Escaneamento de Portas Críticas: Realiza a checagem em portas fundamentais de serviços como SSH, HTTP, HTTPS, MySQL e o próprio PostgreSQL.
Tratamento de Exceções Avançado: Evita travamentos interceptando interrupções do usuário (`KeyboardInterrupt`) e falhas de conexão de rede (`socket.gaierror`).
Pronto para Banco de Dados: Integração nativa com o driver `psycopg2`, permitindo evoluir a ferramenta para salvar logs de auditoria diretamente no PostgreSQL.
Biblioteca socket (Manipulação de conexões TCP/IP)
Psycopg2 (Conexão com Banco de Dados PostgreSQL)
Biblioteca datetime (Registro de data e hora exata)

O que cada porta representa:
Porta 21 (FTP - File Transfer Protocol): Utilizada para transferência de arquivos entre computadores. Versões antigas podem transmitir dados sem criptografia.
Porta 22 (SSH - Secure Shell): Protocolo seguro para acesso e administração remota de servidores. É uma das portas mais visadas para ataques de força bruta.
Porta 53 (DNS - Domain Name System): Responsável por traduzir nomes de domínio (como google.com) em endereços IP.
Porta 80 (HTTP): Protocolo padrão para navegação na web sem criptografia.
Porta 135 (RPC / Microsoft Endpoint Mapper): Utilizada por sistemas Windows para localizar serviços de rede. É monitorada de perto por segurança, 
por casos de vulnerabilidades históricas.
Porta 139 & 445 (SMB - Server Message Block): Portas nativas do Windows usadas para partilha de arquivos e impressoras na rede local. 
Se tornou famosa por ser o vetor de infecção do ransomware *WannaCry*.
Porta 443 (HTTPS): Protocolo seguro para navegação na web, utilizando criptografia SSL/TLS para proteger os dados.
Porta 3306 (MySQL): Porta padrão utilizada pelo sistema de gestão de base de dados MySQL.
Porta 5432 (PostgreSQL): Porta padrão utilizada pelo banco de dados PostgreSQL, relevante para a biblioteca `psycopg2`.
Porta 8000 & 8080 (HTTP Alternate / Web Proxies): São utilizadas por desenvolvedores para testar aplicações web em ambiente de desenvolvimento
(como Django, Flask, ou servidores Tomcat).

Caso queira realizar o teste escaneando a sua própria máquina:
Abra o menu iniciar do Windows, digite cmd e abra o Prompt de Comando.
Digite o comando ipconfig e aperte enter. Procure pela linha Endereço IPv4, esse é o IP que você pode usar como alvo no script.
