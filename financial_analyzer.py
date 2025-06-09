

!pip install phidata
!pip install groq
!pip install python-dotenv
!pip install yfinance
!pip install packaging
!pip install duckduckgo-search
!pip install fastapi
!pip install uvicorn

GROQ_API_KEY="..."
API_KEY="..."


from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to load data"],
    show_tools_calls=True,
    markdown=True,

)

multi_model_agent=Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Use tables to load data"],
    show_tools_calls=True,
    markdown=True,
)

os.environ["GROQ_API_KEY"] = "..."

multi_model_agent.print_response("Summarize analyst recommendations and share the latest news for Tesla", stream=True)