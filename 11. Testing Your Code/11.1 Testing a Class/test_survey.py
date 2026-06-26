import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testing the AnonymousSurvey class"""
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Tonga', 'Nyanja']

    def test_store_single_response(self):
        """Testing that a single response is stored correctly"""
        # question = "What language did you learn?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
        #Here we're using responses in the setup in all test methods
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Testing that three responses are stored correctly"""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Tonga', 'Nyanja']
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()