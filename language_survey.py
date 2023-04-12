from survey import AnonymousSurvey

"""Define a question and make a survey."""
question = 'What language did you first learn to speak?'
language_survey = AnonymousSurvey(question)

"""Save the question and save the responses to the question."""
language_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_responses(response)
"""Show the survey results"""
print("\nThank you to everyone who participated in the survvey!")
language_survey.show_results()