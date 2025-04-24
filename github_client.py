import requests  # Librería para hacer peticiones HTTP
import requests_cache  # Librería para cachear peticiones y evitar llamadas repetidas a la API
from typing import List, Dict  # Tipos para anotaciones
from abc import ABC, abstractmethod  # Para definir una interfaz abstracta

# Instala una caché con duración de 3 horas para las peticiones a GitHub
requests_cache.install_cache('github_cache', expire_after=10.800)


# Interfaz de estrategia para análisis de repositorios
class RepoAnalyzerStrategy(ABC):
    @abstractmethod
    def analyze(self, repo: Dict) -> Dict:
        pass


# Implementación concreta de la estrategia de análisis
class BasicRepoAnalyzer(RepoAnalyzerStrategy):
    def analyze(self, repo: Dict) -> Dict:
        return {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "url": repo["html_url"]
        }


# Cliente para interactuar con la API de GitHub
class GitHubClient:
    BASE_URL = "https://api.github.com" # URL base de la API

    def __init__(self):
        # Crea una sesión de requests para reutilizar conexiones
        self.session = requests.Session()

    def search_repositories(self, keywords: List[str], language: str = None, limit: int = 10, sort: str = "stars") -> List[Dict]:
        # Construye la consulta de búsqueda
        query = " ".join(keywords)
        if language:
            query += f" language:{language}"

        # Llama a la API de búsqueda de repositorios
        url = f"{self.BASE_URL}/search/repositories"
        params = {"q": query, "sort": sort, "order": "desc", "per_page": limit}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json().get("items", [])

    def get_commits(self, owner: str, repo: str) -> List[Dict]:
        # Obtiene los commits más recientes del repositorio
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        response = self.session.get(url, params={"per_page": 5})
        response.raise_for_status()
        return response.json()

    def get_contributors(self, owner: str, repo: str) -> List[Dict]:
        # Obtiene la lista de contribuidores al repositorio
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/contributors"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_open_issues(self, owner: str, repo: str) -> List[Dict]:
        # Obtiene las issues abiertas del repositorio
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        response = self.session.get(url, params={"state": "open"})
        response.raise_for_status()
        return response.json()
