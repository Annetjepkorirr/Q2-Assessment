# // **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# // down from generation to generation. Imagine you're creating an application that
# // records these oral stories and translates them into different languages. The
# // stories vary by length, moral lessons, and the age group they are intended for.
# // Think about how you would model `Story`, `StoryTeller`, and `Translator`
# // objects, and how inheritance might come into play if there are different types of
# // stories or storytellers.

# // pseudo code
# // input    length of the story     
#             // moral lessons
#             //agegroup

# // output     storytelling

# // process      create classes-StoryTelling
#                 // constructor


class StoryTeller: 
    def __init__(self,name, language):
      self.name = name
      self.language = language
    
  
    def tellStory(story):
      return f"Hello, I am {self.name} and my story for toaday will be from {self.language}"
  
  
#   Implement a class called Student with attributes for name, age, and grades (a
#     list of integers). Include methods to calculate the average grade, display the
#     student information, and determine if the student has passed (average grade >=
#     60). Create objects for the Student class and demonstrate the usage of these
#     methods.

class Student:
    def __init__(self,name,age,grades):
        self.name =  name
        self.age = age
        self.grades = grades
        
 
            
       
      
      


