import os
from dotenv import load_dotenv

# Carga el archivo .env si existe
load_dotenv()

# Lee las claves desde variables de entorno
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Verifica que existan
if not COMPOSIO_API_KEY:
    raise EnvironmentError(
        "COMPOSIO_API_KEY no está definido. Por favor crea un archivo .env o exporta la variable de entorno."
    )

if not OPENAI_API_KEY:
    raise EnvironmentError(
        "OPENAI_API_KEY no está definido. Por favor crea un archivo .env o exporta la variable de entorno."
    )

print("COMPOSIO_API_KEY cargado correctamente.")
print("OPENAI_API_KEY cargado correctamente.")
