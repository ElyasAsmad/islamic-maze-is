class QuestionSet:
    def __init__(self, question: str, answer: list[str]):
        self.question = question
        self.answer = answer
        
    def get_answer_list(self):
        return self.answer
      
questions = [
    QuestionSet('What is the name of the Islamic charity given during the month of Ramadan?', ['Zakat', 'Zakt']),
    QuestionSet('In what city is the Kaaba located?', ['Mecca', 'Mekah']),
    QuestionSet('What is the first qibla for muslims?', ['Al-Aqsa Mosque', 'Masjid Al-Aqsa', 'Al-Aqsa', 'al aqsa']),
]