import sys
import os

# Agrega el directorio padre (Generalist_Trigger_Test) al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MCP.MCP_Client import load_mcp_tools
from AGENT import create_langgraph_agent


tools = load_mcp_tools()
agent = create_langgraph_agent(tools)

# Prueba básica
prompt = "Escribe un correo de prueba para saludar."
response = agent.invoke({"input": prompt})
print("Respuesta del agente:", response)
