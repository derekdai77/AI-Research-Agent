# Architecture

## Overview
- **ResearchAgent** orchestrates the entire research workflow.
- **ReActAgent** manages step-by-step decisions (ReAct approach).
- **ReportAgent** assembles the final data into a user-friendly report.

## Data Flow
1. **Input**: A topic to explore.
2. **ReActAgent**: Iteratively decides which tools to use (SerpAPI, ArXiv, etc.).
3. **ReportAgent**: Summarizes and finalizes the collected data.
