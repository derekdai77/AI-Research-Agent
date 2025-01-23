import openai
import json
from tools.arxiv_fetch import fetch_papers
from tools.serpapi_search import perform_search
from tools.rag_search import retrieve_information

class ReActAgent:
    '''
    This agent follows a simplified ReAct (Reason+Act) approach:
    1) Gathers partial observations.
    2) Produces reasoning steps.
    3) Decides which tool(s) to call next.
    4) Iterates until it deems it has enough info.
    '''

    def __init__(self, config, graph):
        self.config = config
        self.graph = graph                     
        openai.api_key = config['services']['openai']['api_key']

        self.graph.add_node("ReActAgent")

    def run_react_loop(self, topic, max_iterations=3):
        '''
        Simplified ReAct loop:
        1) Start with a prompt about the topic.
        2) Reason about the next best tool call.
        3) Gather partial results.
        4) Continue or stop.
        '''
        context = f"Topic: {topic}\nWe are collecting data from various tools: SerpAPI, ArXiv, RAG."
        collected_data = []

        self.graph.set_node_data("ReActAgent", {"context": context})

        for i in range(max_iterations):
            action = self.decide_action(context)
            if not action:
                # If the model decides it has enough info, break
                break

            tool_name, data = self.execute_action(action, topic)
            collected_data.append({tool_name: data})

            node_id = f"ReActAgent-Step{i+1}-{tool_name}"
            self.graph.add_node(node_id, data={"tool": tool_name, "data": data})

            self.graph.add_edge("ReActAgent", node_id, label=f"Step {i+1}")

ß            self.graph.add_edge(node_id, "ReActAgent", label="Result feedback")

            # Expand context with newly retrieved data
            context += f"\nTool used: {tool_name}\nData: {data}"

        # Combine all data into a single string
        final_data = ""
        for item in collected_data:
            for tool_name, output in item.items():
                final_data += f"\n=== {tool_name.upper()} OUTPUT ===\n{output}\n"

        return final_data

    def decide_action(self, context):
        '''
        Ask GPT-like model: Should we query a tool or stop?
        For demonstration, the naive cycle: SerpAPI -> ArXiv -> RAG -> stop.
        '''
        if "SERPAPI" not in context.upper():
            return "SERPAPI_SEARCH"
        elif "ARXIV" not in context.upper():
            return "ARXIV_FETCH"
        elif "RAG" not in context.upper():
            return "RAG_SEARCH"
        else:
            return None  # Indicate we have enough info

    def execute_action(self, action, topic):
        '''
        Call the chosen tool to get partial results.
        '''
        if action == "SERPAPI_SEARCH":
            data = perform_search(topic, self.config['services']['serpapi']['api_key'])
            return ("serpapi", data)

        elif action == "ARXIV_FETCH":
            papers = fetch_papers(topic, self.config['services']['arxiv']['api_url'])
            return ("arxiv", papers)

        elif action == "RAG_SEARCH":
            search_results = perform_search(topic, self.config['services']['serpapi']['api_key'])
            papers = fetch_papers(topic, self.config['services']['arxiv']['api_url'])
            info = retrieve_information(search_results, papers)
            return ("rag", info)

        return (action.lower(), "No action performed.")
