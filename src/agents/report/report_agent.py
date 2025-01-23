import openai

class ReportAgent:
    '''
    This agent takes the final set of information gathered by the ReActAgent
    and transforms it into a user-friendly research report.
    '''

    def __init__(self, config):
        self.config = config
        openai.api_key = config['services']['openai']['api_key']

    def generate_report(self, collected_data, topic):
        '''
        Summarize all the data into a cohesive report about `topic`.
        '''
        system_prompt = "You are a helpful AI that crafts well-structured research summaries."
        user_prompt = f"Create a comprehensive, user-friendly research report on: {topic}.\nData collected:\n{collected_data}"

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=3000,
            temperature=0.7
        )

        return response.choices[0].message['content']
