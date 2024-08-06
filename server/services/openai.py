from server.core.agent import Agent
from server.sql.schemas import ChatRequestBody, ChatResponseBody


def agent_chat(chat_msg: ChatRequestBody):
    resp = ChatResponseBody()
    resp.aiMessage = Agent().chat(chat_msg.humanMessage)
    return resp
