import yaml
from agents.research_agent import ResearchAgent
from utils.helpers import save_report

def load_config():
    with open('configs/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    research_agent = ResearchAgent(config)

    print("Welcome to the Multi-Agent Research System!")
    topic = input("Enter a research topic to explore: ")

    # Run the multi-step research
    final_report = research_agent.conduct_research(topic)

    print("\n=== FINAL RESEARCH REPORT ===")
    print(final_report)

    # Optionally save the report
    save_report(final_report, filename='research_report.txt')

if __name__ == "__main__":
    main()
