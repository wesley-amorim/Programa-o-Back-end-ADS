import requests

def validarSite(url):
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            print(f"Código de status: {resposta.status_code} - Site Operacional")
        else:
            print(f"Código de status: {resposta.status_code} - Site com Problemas")
    
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível acessar a aplicação: {e}")

while True:
    #.strip() para evitar erros de espaçamento antes ou depois da url
    url_site = input("Digite o site que deseja verificar (ex: qualquercoisa.com) ou digite 'sair' para encerrar: ").strip()
    
    #.lower() para não ter problemas ao digitar sair com letras maiúsculas e minúsculas
    if url_site.lower() == 'sair':
        print("Fim da Aplicação, Obrigado!")
        break

    # Adiciona o prefixo 'https://www.' se o usuário não digitar nada no início
    if not url_site.startswith('https://'):
        url_site = 'https://www.' + url_site

    # Chama a função
    validarSite(url_site)
