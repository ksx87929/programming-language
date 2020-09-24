##
#  This module defines a hierarchy of classes that model exam questions. 
#

## A question with a text and an answer.
#
class Question :
   ## Constructs a question with empty question and answer strings.
   #
   def __init__(self) :
      self._text = ""
      self._answer = ""
      self._text4 = ""
   ##  Sets the question text.
   #   @param questionText the text of this question
   #
   def setText(self, questionText) :   
      self._text = questionText   
      
   def setText4(self, questionText) :   
      self._text4 = questionText

   ## Sets the answer for this question.
   #  @param correctResponse the answer
   #
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse
      
   def setMultiAnswer(self, correctResponse) :
      self._answer += correctResponse
      
   def checknumAnswer(self, response) :
      response=float(response)
      self._answer=float(self._answer)
      temp = response - self._answer
      if temp <= 0.01 and temp >= -0.01 :
          return True
      else :
          return False
   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
      return response == self._answer
  
   def checkMultiAnswer(self, response) :
       A=""
       temp=""
       for i in range(len(response)) :
           if response[i]!=' ' :
               temp+=response[i]
       for x in sorted(temp) :
           A+=x
       return A==self._answer
    
   ## Displays this question.
   #
   def display(self) :
      print(self._text)
      
   def display4(self) : 
      return(self._text4)
      
## A question with multiple choices.
#
class ChoiceQuestion(Question, object) :
   # Constructs a choice question with no choices.
   def __init__(self) :
      super(ChoiceQuestion, self).__init__()
      self._choices = []

   ## Adds an answer choice to this question.
   #  @param choice the choice to add
   #  @param correct True if this is the correct choice, False otherwise
   #
   def addChoice(self, choice, correct) :
      self._choices.append(choice)
      if correct :
         # Convert len(choices) to string.
         choiceString = str(len(self._choices))
         self.setAnswer(choiceString)
   
   # Override Question.display().
   def display(self) :
      # Display the question text.
      super(ChoiceQuestion, self).display()
      
      # Display the answer choices.
      for i in range(len(self._choices)) :
         choiceNumber = i + 1
         print("%d: %s" % (choiceNumber, self._choices[i]))
            
class NumericQuestion(Question) :
    def __init__(self) :
        super(NumericQuestion , self).__init__()
        
class FillInQuestion(Question) :
    def __init__(self) :
        super(FillInQuestion,self).__init__()

class MultiChoiceQuestion(Question) :
    def __init__(self) :
        super().__init__()
        self._multichoices = []
        
    def addMultiChoice (self,choice,correct) :
        self._multichoices.append(choice)
        if correct :
            mutichoiceString = str(len(self._multichoices))
            self.setMultiAnswer(mutichoiceString)
            #self.setAnswer(" ")
            
    def display(self) :
        # Display the question text.
      super(MultiChoiceQuestion, self).display()
      
      # Display the answer choices.
      for i in range(len(self._multichoices)) :
         multichoiceNumber = i + 1
         print("%d: %s" % (multichoiceNumber, self._multichoices[i]))