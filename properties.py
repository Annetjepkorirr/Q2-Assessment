class Artist:
    def __init__(self, name, country, music_style, instrument):
        self.name = name
        self.country = country
        self.music_style = music_style
        self.instrument = instrument
    def display_details(self):
        return f'Name: {self.name}, Country: {self.country}, Music Style: {self.music_style}, Instrument: {self.instrument}'
class Performance(Artist):
    def __init__(self, name, country, music_style, instrument, end_time, start_time):
        super().__init__(name, country, music_style, instrument)
        self.end_time = end_time
        self.start_time = start_time
    def performance_duration(self):
        total_time = {self.end_time} - {self.start_time}
        return total_time
        # return f"{self.end_time} - {self.start_time}"
class Stage(Artist):
    def __init__(self, name, country, music_style, instrument, location):
        super().__init__(name, country, music_style, instrument)
        self.location = location
        self.schedule = []
        
    def lineApp(self, activity):
        self.schedule.append(activity)
# instance of the Artist class
artist = Artist("Quavo", "Carlifornia", "break dancing", "guiter")
print(artist.display_details())
# instance of the Performance class
performance = Performance("Drake", "Las Vegas", "Pop", "Vocals", "10:00","8:00")
print(performance.performance_duration())
# instance of the Stage class
stage = Stage("Gengetone", "Kenya", "raping", "gutar", "hall")
stage.lineApp("dance hall")
print(stage.schedule)


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        return f"name:{self.name},age:{self.age},average:{self.calculate_average_grade()}"
        # print(f"Name: {self.name}")
        # print(f"Age: {self.age}")
        # print(f"Grades: {self.grades}")

    def has_passed(self):
         average = self.calculate_average_grade()
         if average >= 50:
             return f"{self.name}: passed"
         else:
             return f"{self.name}: is below average"
       
# Creating objects for the Student class
student1 = Student("John Doe", 18, [80, 75, 90, 85])
student2 = Student("Jane Smith", 17, [70, 65, 80, 75])

# Demonstrating the usage of methods
student1.display_student_info()
print(f"Average Grade: {student1.calculate_average_grade()}")
print(f"Has Passed: {student1.has_passed()}")

student2.display_student_info()
print(f"Average Grade: {student2.calculate_average_grade()}")
print(f"Has Passed: {student2.has_passed()}")