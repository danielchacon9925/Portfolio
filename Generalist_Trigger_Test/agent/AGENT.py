# Agent script
# API KEY
from langgraph.graph import StateGraph, END
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

import config

def create_langgraph_agent(tools):
    # Inicializa modelo OpenAI con tu API key
    llm = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
    
    memory = ConversationBufferMemory()
    
    # Inicializa agente con herramientas
    agent_executor = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )
    
    # Crea grafo de estados
    workflow = StateGraph()
    
    # Agrega un nodo "agent" que ejecuta el agente
    workflow.add_node("agent", agent_executor.invoke)
    
    # Nodo de inicio y finalización
    workflow.set_entry_point("agent")
    workflow.set_finish_point("agent")
    
    # Devuelve el workflow compilado
    return workflow.compile()
