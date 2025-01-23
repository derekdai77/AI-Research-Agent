import unittest
from src.agents.research_agent import ResearchAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.fake_config = {
            "services": {
                "openai": {"api_key": "fake-openai-key"},
                "serpapi": {"api_key": "fake-serpapi-key"},
                "arxiv": {"api_url": "http://export.arxiv.org/api/query"}
            }
        }
        self.agent = ResearchAgent(self.fake_config)

    def test_conduct_research(self):
        topic = "Test Topic"
        result = self.agent.conduct_research(topic)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
