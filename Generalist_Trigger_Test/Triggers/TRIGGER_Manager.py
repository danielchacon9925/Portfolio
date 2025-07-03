from flask import Flask, request
from agent.AGENT import create_langgraph_agent
from MCP.MCP_Client import load_mcp_tools

app = Flask(__name__)
tools = load_mcp_tools()
agent = create_langgraph_agent(tools)


@app.route('/webhook/email', methods=['POST'])
def handle_email_trigger():
    data = request.json
    subject = data.get("subject", "")
    body = data.get("body", "")
    user_input = f"Responder este correo:\nAsunto: {subject}\nCuerpo: {body}"

    result = agent.invoke({"input": user_input})
    return {"status": "ok", "response": result}


if __name__ == '__main__':
    app.run(port=5000)
