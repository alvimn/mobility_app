
from github_client import GitHubClient  # Importa el cliente de GitHub para interactuar con la API
import argparse  # Para analizar argumentos de línea de comandos
from github_client import BasicRepoAnalyzer  # Estrategia de análisis simple de repositorios
import requests  # Para manejar errores HTTP al interactuar con la API de GitHub
import time  # Para pausar entre peticiones y evitar rate limiting


def main():
    # Imprime mensaje inicial
    print("\nQue palabras quieres usar\n")

    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Analizador de repositorios de transporte en GitHub")

    # Argumento opcional: lenguaje de programación
    parser.add_argument("--language", type=str, help="Filtrar por lenguaje de programación (opcional)")

    # Argumento opcional: lista de palabras clave con default la lista proporcionada
    parser.add_argument("--keywords", nargs="+", default=["taxi", "ride-sharing", "transportation", "mobility"],
                        help="Lista de palabras clave para buscar repositorios")

    # Argumento opcional: límite de resultados
    parser.add_argument("--limit", type=int, default=10, help="Cantidad de repositorios a mostrar (máx 100)")

    # Argumento opcional: orden de descarga
    parser.add_argument("--sort", type=str, help="Filtrar por orden que seguir (opcional)", default="stars")
    
    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()

    # Instancia el analizador y cliente de GitHub
    analyzer = BasicRepoAnalyzer()
    client = GitHubClient()

    print("\nBuscando repositorios...\n")

    # Realiza búsqueda de repositorios según los parámetros ingresados
    repos = client.search_repositories(keywords=args.keywords, language=args.language, limit=args.limit, sort=args.sort)

    # Itera sobre los repositorios encontrados
    for repo in repos:
        # Analiza el repositorio para extraer datos básicos
        info = analyzer.analyze(repo)
        owner = repo["owner"]["login"]
        name = repo["name"]

        try:
            # Intenta obtener datos adicionales: commits, contribuidores e issues
            commits = client.get_commits(owner, name)
            contributors = client.get_contributors(owner, name)
            issues = client.get_open_issues(owner, name)
        except requests.HTTPError as e:
            # En caso de error, imprime mensaje y continúa con el siguiente repositorio
            print(f"\nError al obtener detalles de {name}: {e}\n")
            continue

        # Imprime la información del repositorio
        print(f"Nombre: {info['name']}")
        print(f"Estrellas: {info['stars']}")
        print(f"Lenguaje: {info['language']}")
        print(f"URL: {info['url']}")
        print(f"Commits recientes: {len(commits)}")
        print(f"Contribuidores: {len(contributors)}")
        print(f"Issues abiertas: {len(issues)}")
        print("-" * 40)

        # Pausa entre peticiones para evitar restricciones de la API
        time.sleep(1)