import logging

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from server.core.config import Config

logger = logging.getLogger(__name__)


class Agent(object):
    def __new__(cls):
        """
        单例模式初始化
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Agent, cls).__new__(cls)
            cls.instance._init()
        return cls.instance

    def _init(self):
        Config().load_config()
        self.model = ChatOpenAI(
            base_url=Config().config_dict["chat.api_url"],
            api_key=Config().config_dict["chat.api_key"],
            model=Config().config_dict["chat.api_model"]
        )

        system_template = "你是一个nuclei poc 模板编写专家，请根据http流，帮我编写 nuclei poc 模板。【poc模板除外，禁止回答其他内容】"
        user_template = "{user_input}"

        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", user_template)]
        )

        parser = StrOutputParser()
        self.chain = prompt_template | self.model | parser

    def chat(self, human_message):
        logger.debug(human_message)
        response = self.chain.invoke({"user_input": human_message})
        logger.debug(f"Response: {response}l")
        return response
