# AI Research Agent with Multiple Interconnected Agents & ReAct

## Overview

This project demonstrates a multi-agent AI research workflow, leveraging [ReAct-style](https://arxiv.org/abs/2210.03629) reasoning-and-acting patterns, **LangGraph**, and various tools (e.g., SerpAPI, ArXiv, RAG). Multiple agents collaborate to produce **in-depth research reports**, offering a robust user experience.

### Key Agents

1. **ReActAgent**: A chain-of-thought agent that decides which tools to call, step by step.
2. **ResearchAgent**: Oversees the high-level research workflow and delegates tasks to other agents.
3. **ReportAgent**: Gathers final results and shapes them into a coherent report.

### Tools

- **ArXiv Tool**: Fetches scientific papers.
- **Google SerpAPI Tool**: Performs web searches.
- **RAG Search**: Retrieves relevant info from combined search results and papers.

## Setup & Installation

```bash
# 1) Clone or Download Project
git clone https://github.com/USERNAME/AI-Research-Agent.git
cd AI-Research-Agent

# 2) Create Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# 3) Install Dependencies
pip install -r requirements.txt

# 4) Configure Secrets
cp configs/secrets.yaml.example configs/secrets.yaml
# Edit configs/secrets.yaml to add your actual API keys

# 5) Run the Main Script
python src/main.py
```

## Usage

1. **Start the app**: `python src/main.py`
2. **Enter a research topic** when prompted (e.g., "Quantum Computing").
3. The system orchestrates multiple agents:
   - The **ResearchAgent** sets up the stage.
   - The **ReActAgent** decides *if and when* to call tools (SerpAPI, ArXiv, etc.).
   - The **ReportAgent** compiles a final, user-friendly research report.

## Contributing

Feel free to open issues or create pull requests for improvements and fixes.

## License

This project is licensed under the [MIT License](LICENSE).

