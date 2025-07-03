import config
from composio_langchain import ComposioToolSet


def load_mcp_tools():
    toolkit = ComposioToolSet(api_key=config.COMPOSIO_API_KEY)
    tools = toolkit.get_tools(["GMAIL_FETCH_EMAILS", "GMAIL_SEND_EMAIL"])
    return (tools)

#import config

#def load_mcp_tools():
#    toolkit = ComposioToolSet(api_key=config.COMPOSIO_API_KEY)
    
    # Intenta obtener la lista de herramientas disponibles
#    all_tools = toolkit.get_tools()  # Sin parámetros, intenta traer todas las herramientas
    
    # Imprime las herramientas para ver qué hay
#    print("Herramientas disponibles:", all_tools)
    
#    return all_tools

#if __name__ == "__main__":
#    load_mcp_tools()
