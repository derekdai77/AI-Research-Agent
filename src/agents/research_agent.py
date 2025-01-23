import openai
from agents.react.react_agent import ReActAgent
from agents.report.report_agent import ReportAgent

class ResearchAgent:
    def __init__(self, config):
        self.config = config
        openai.api_key = config['services']['openai']['api_key']

        self.react_agent = ReActAgent(config)
        self.report_agent = ReportAgent(config)

    def conduct_research(self, topic):
        # 1) Use ReAct Agent to gather relevant data step-by-step
        interim_results = self.react_agent.run_react_loop(topic)

        # 2) Finalize the data into a user-friendly report
        final_report = self.report_agent.generate_report(interim_results, topic)
        return final_report
