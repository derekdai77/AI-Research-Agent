# src/agents/research_agent.py

import openai
from langgraph import LangGraph
from agents.react.react_agent import ReActAgent
from agents.report.report_agent import ReportAgent

class ResearchAgent:
    def __init__(self, config):
        self.config = config
        openai.api_key = config['services']['openai']['api_key']

        # 初始化 LangGraph
        self.graph = LangGraph(
            name="Multi-Agent Workflow",
            description="Visualize the flow between ReActAgent, ReportAgent, and tool calls."
        )

        # 初始化其他 Agent
        self.react_agent = ReActAgent(config, self.graph)   # <-- 传入 graph 方便 ReActAgent 使用
        self.report_agent = ReportAgent(config)

    def conduct_research(self, topic):
        # 在 LangGraph 中注册/添加节点，用于表示 ResearchAgent
        self.graph.add_node("ResearchAgent", data={"topic": topic})

        # 1) 用 ReActAgent 多步搜集信息
        interim_results = self.react_agent.run_react_loop(topic)

        # 把 ReActAgent 的输出暂存到 Graph
        self.graph.set_node_data("ResearchAgent", {"interim_results": interim_results})

        # 2) 用 ReportAgent 生成最终报告
        final_report = self.report_agent.generate_report(interim_results, topic)

        # 把生成的报告也放到图中
        node_data = self.graph.get_node_data("ResearchAgent") or {}
        node_data["final_report"] = final_report
        self.graph.set_node_data("ResearchAgent", node_data)

        # 也可添加 ReportAgent 节点，并创建和 ResearchAgent 节点的边
        self.graph.add_node("ReportAgent")
        self.graph.add_edge("ResearchAgent", "ReportAgent", label="Generate final report")
        self.graph.set_node_data("ReportAgent", {"report": final_report})

        return final_report
