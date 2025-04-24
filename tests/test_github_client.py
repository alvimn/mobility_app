from github_client import GitHubClient

def test_buscar():
    client = GitHubClient()
    resultado = client.buscar_repositorios("taxi")
    assert isinstance(resultado, list)
