import requests

print("Acessando API pública e estável de vagas de Tecnologia...")

# Endpoint global aberto de vagas de TI (focado em trabalho remoto e tecnologia)
url = "https://www.arbeitnow.com/api/job-board-api"

try:
    # Faz a requisição direta (sem navegador, sem risco de captchas)
    resposta = requests.get(url, timeout=10)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        vagas = dados.get("data", [])
        
        print(f"Sucesso! Foram encontradas {len(vagas)} vagas de TI em tempo real.\n")
        print("========== VAGAS EXTRAÍDAS PARA O SEU SITE ==========\n")
        
        # Filtro de cargos igual à lógica do seu professor
        palavras_chave = ["engineer", "developer", "analyst", "tech", "manager", "data", "software", "dev"]
        
        for i, vaga in enumerate(vagas):
            titulo = vaga.get("title", "Não informado")
            empresa = vaga.get("company_name", "Não informado")
            local = vaga.get("location", "Remoto")
            # Convertendo os tópicos da vaga em uma descrição curta
            tags = ", ".join(vaga.get("tags", []))
            descricao = f"Tags da vaga: {tags}." if tags else "Vaga para profissionais de Tecnologia."
            
            # Valida se o título possui palavras-chave de TI
            if any(termo in titulo.lower() for termo in palavras_chave):
                print(f"VAGA {i+1}")
                print(f"Cargo: {titulo}")
                print(f"Empresa: {empresa}")
                print(f"Localização: {local}")
                print(f"Descrição: {descricao}")
                print("-" * 50)
                
    else:
        print(f"Erro ao acessar o servidor. Código de status: {resposta.status_code}")

except Exception as e:
    print(f"Erro na conexão: {e}")

print("\nProcesso finalizado!")