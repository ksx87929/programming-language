##
#  This program shows a simple quiz with two question types.
#

from questions import Question, ChoiceQuestion ,NumericQuestion ,FillInQuestion ,MultiChoiceQuestion

def main() :
   first = Question()
   first.setText("Who was the inventor of Python?")
   first.setAnswer("Guido van Rossum")

   second = ChoiceQuestion()
   second.setText("In which country was the inventor of Python born?")
   second.addChoice("Australia", False)
   second.addChoice("Canada", False)
   second.addChoice("Netherlands", True)
   second.addChoice("United States", False)
   
   third = NumericQuestion()
   third.setText("How much is 1 + 1")
   third.setAnswer("2")
   
   fourth = FillInQuestion()
   fourth.setText("The inventor of Python was _____")
   fourth.setText4("The inventor of Python was")
   fourth.setAnswer("Guido van Rossum")
   
   fifth = MultiChoiceQuestion()
   fifth.setText("In which fruit is red?")
   fifth.addMultiChoice("Apple", True)
   fifth.addMultiChoice("Orange", False)
   fifth.addMultiChoice("Tomato", True)
   fifth.addMultiChoice("guava", False)
   
   
   #presentQuestion(first)
   #presentQuestion(second)
   present3Question(third)
   present4Question(fourth)
   present5Question(fifth)

## Presents a question to the user and checks the response.
#  @param q the question
#
def presentQuestion(q) :
   q.display()   # Uses dynamic method lookup.
   raw_input=input("Your answer is : ")
   response = raw_input
   print(q.checkAnswer(response))   # checkAnswer uses dynamic method lookup.
   
# Start the program.
def present3Question(q) :
   q.display()   # Uses dynamic method lookup.
   raw_input=input("Your answer is : ")
   response = raw_input
   print(q.checknumAnswer(response)) 
   
def present4Question(q) :
   q.display()   # Uses dynamic method lookup.
   raw_input=input("Your answer is : ")
   response = raw_input
   if q.checkAnswer(response) :
       print(q.display4(),"_",response,"_")
   else :
       print("False")
def present5Question(q) :
   q.display()   # Uses dynamic method lookup.
   raw_input=input("Your answer is : ")
   response = raw_input
   print(q.checkMultiAnswer(response))
main()
