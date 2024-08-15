from dotenv import load_dotenv

load_dotenv()

from lavague.core import WorldModel, ActionEngine
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from lavague.core.agents import WebAgent
from lavague.drivers.selenium import SeleniumDriver

mm_llm = OpenAIMultiModal(model="gpt-4o-mini")

selenium_driver = SeleniumDriver(headless=False)
world_model = WorldModel(mm_llm=mm_llm)
action_engine = ActionEngine(selenium_driver)
agent = WebAgent(world_model, action_engine)
agent.get("https://chandlerroth.com")
agent.run("Extract all links from the page")
