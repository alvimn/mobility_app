#  GitHub Transport Repo Analyzer

Este proyecto permite buscar y analizar repositorios públicos en GitHub relacionados con transporte, movilidad, taxis, ride-sharing y más. Utiliza la API de GitHub y ofrece información relevante como estrellas, lenguaje, contribuidores, issues abiertas y commits recientes.

##  ¿Qué hace?

- Busca repositorios con palabras clave y filtro por lenguaje.
- Muestra estadísticas básicas del repositorio (estrellas, lenguaje, URL).
- Muestra número de contribuidores.
- Muestra cantidad de issues abiertas.
- Recupera commits recientes, usando caché local para evitar llamadas repetidas a la API.

---

## Instala las dependencias:
pip install -r requirements.txt

## Uso
Ejecuta el script desde la terminal:

bash <br>
Copy <br>
Edit <br>
python main.py --language python --keywords taxi ride-sharing --limit 5 <br>
### Argumentos:
|   Opción   |                     Descripción                    | Requerido |              Valor por defecto             |
|:----------:|:--------------------------------------------------:|:---------:|:------------------------------------------:|
| --language | Lenguaje de programación para filtrar repositorios | ❌         | -                                          |
| --keywords | Palabras clave a buscar (puedes pasar varias)      | ❌         | ["taxi", "ride-sharing", "transportation"] |
| --limit    | Máximo número de repositorios a mostrar (máx 100)  | ❌         | 10                                         |
| --sort     | Orden por el cual va ha buscar                     | ❌         | "stars"                                    |

## Ejemplo de Salida

Buscando repositorios...

Nombre: awesome-taxi-data <br>
Estrellas: 1523 <br>
Lenguaje: Python <br>
URL: https://github.com/user/awesome-taxi-data <br>
Commits recientes: 5 <br>
Contribuidores: 12 <br>
Issues abiertas: 3 <br>
## Test unitarios 
Ejecutar el script desde la terminal:  <br>
python -m unittest test_github_client.py -v

----------------------------------------
