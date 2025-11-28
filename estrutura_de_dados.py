# =======================================================
# PYTHON-FUNDAMENTOS
# Script para demonstrar estruturas de dados básicas (Listas e Dicionários)
# Essencial para manipular dados em projetos de IA/ML
# =======================================================

# 1. LISTA: Estrutura de dados ordenada e mutável.
# Exemplo: Lista de frameworks de IA que estou estudando.
frameworks_ia = ["LangChain", "OpenAI", "Google Gemini", "Scikit-learn", "Pandas"]
print(f"Lista de Frameworks: {frameworks_ia}")

# Acessando um item específico da lista
print(f"Framework principal para LLMs: {frameworks_ia[0]}")

# 2. DICIONÁRIO: Estrutura de dados desordenada (Chave: Valor).
# Exemplo: Mapeando conceitos de Machine Learning.
conceitos_ml = {
    "Algoritmo": "Conjunto de regras para resolver um problema.",
    "Data Preprocessing": "Limpeza e preparação de dados para um modelo.",
    "Modelo": "Saída de um algoritmo de Machine Learning executado sobre dados."
}

# Imprimindo um conceito do dicionário
print("\nConceitos de ML:")
for chave, valor in conceitos_ml.items():
    print(f"- {chave}: {valor}")

# 3. LOOPS (Iteração): Usado para processar grandes volumes de dados (listas, dicionários).
print("\nIterando sobre a lista de frameworks:")
for framework in frameworks_ia:
    print(f"Estudando: {framework}")

# Fim do script de fundamentos.
