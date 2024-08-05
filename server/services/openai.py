from server.core.agent import Agent
from server.sql.schemas import ChatRequestBody, ChatResponseBody


def agent_chat(chat_msg: ChatRequestBody):
    agent = Agent()
    ai_msg = agent.chat(chat_msg.human_message)

    resp = ChatResponseBody()
    resp.ai_message = ai_msg
    return resp
