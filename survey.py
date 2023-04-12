class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_responses):
        """Store a single response to the survey"""
        self.responses.append(new_responses)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
            