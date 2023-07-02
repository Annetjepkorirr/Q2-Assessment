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


class Story:
  def __init__(self,title,length,moral_lessons,age_group):
    self.title  = title
    self.length = length
    self.moral_lessons = moral_lessons
    self.age_group = age_group
  
  def display_story():
    return f"The story titled {self.title} is intresting"  
     
class StoryTeller(Story):
  def __init__(self, title, length, moral_lessons, age_group,name):
    super().__init__(title, length, moral_lessons, age_group)
    self.name = name
     
  def tell_story(self):
    return f"The story that {self.name} narrated titled, {self.title} has good lesson that we should  {self.moral_lessons} and it is meant for {self.age_group}"
    
    
class Translator:
  def __init__(self,language,name):
    self.language = language
    self.name = name
    
    
  def get_translation(self):
    return f"{self.name} is able to tranlate stories to {self.language}"
    
    
story1 = StoryTeller("Hyena and Elephant",100,"Not to be mean","adults","Mzee")
print(story1.tell_story())

translator = Translator("Agikuyu","Jane")
print(translator.get_translation())


# class Recipes:
#   def __init__(self,name,ingredients,preparationTime,cookingMethod,nutritionalInformation):
#     self.name =  name
#     self.ingredients = ingredients
#     self.preparationTime = preparationTime
#     self.cookingMethod = cookingMethod
#     self.nutritionalInformation = nutritionalInformation
    
#   def recipes(self):
#     return f"When preparing {self.name} the following ingredients are required,{self.ingredients}, you will need {self.preparationTime} and the cooking method is to {self.cookingMethod} and it makes {self.nutritionalInformation}"
      

# class MoroccoanRecipe(Recipes):
#   def __init__(self, name,ingredients,preparationTime,cookingMethod,nutritionalInformation,spices):
#     super().__init__(name,ingredients,preparationTime,cookingMethod,nutritionalInformation)
#     self.spices =spices
    
#   def spicy_foods(self):
#     return f"{self.name} has different ingredients for tacos preparations such as {self.ingredients}.  You require a maximum of {self.preparationTime}. You will additionally need {self.spices} to make it more tastier"
    
    
# class EthiopianRecipe(Recipes):
#   def __init__(self, name,ingredients,preparationTime,cookingMethod,nutritionalInformation,taste):
#     super().__init__(name,ingredients,preparationTime,cookingMethod,nutritionalInformation)
#     self.taste = taste  
    
#   def tasty_foods(self):
#     return f"{self.name} has different ingredients for cake preparations such as {self.ingredients}. Time required is {self.preparationTime}. To add more taste you will require more toppings to make it {self.taste}" 
  
# class NigerianRecipe(Recipes):
#   def __init__(self, name,ingredients,preparationTime,cookingMethod,nutritionalInformation,feel):
#     super().__init__(name,ingredients,preparationTime,cookingMethod,nutritionalInformation)
#     self.feel = feel  
    
#   def foods(self):
#     return f"{self.name} has different ingredients for cake preparations such as {self.ingredients}. Time required is {self.preparationTime}. To add more taste you will require more toppings to make you feel {self.feel}" 
    
    
  
# foods = Recipes("Grilled chicken","Cumin powder,tumeric and soysauce","60minutes","simmer","makes bone strong")
# print(foods.recipes())
  
# moroccoan_dish = MoroccoanRecipe("Moroccoan food","flour","30minutes","simer","makes the body strong","black pepper")
# print(moroccoan_dish.spicy_foods())

# ethiopian_dish =EthiopianRecipe("Ethiopian food","vanilla essence","120minutes","adding floor, more sugar as you stir","strength","finger licking")
# print(ethiopian_dish.tasty_foods())

# nigerian_dish = NigerianRecipe("Nigerian food","strawberry essence","90minutes","boiling water","Keeps the body free from nutrinional diseases","energetic")
# print(nigerian_dish.foods())
     
     
     
# class Recipe:
#         def __init__(self,ingredients,preparation_time,cooking_method,nutritional_information):
#          self.ingredients=ingredients
#          self.preparation_time=preparation_time
#          self.cooking_method=cooking_method
#          self.nutrtional_information=nutritional_information

#         def recipe(self):
#             return f"The recipe has the following {self.ingredients} it takes {self.preparation_time} to prepare it also cooked by  {self.cooking_method} and {self.nutrtional_information}"
# recipe1=Recipe(ingredients=['flour' ,'eggs' ,'sugar', 'milk'],preparation_time='30minutes',cooking_method='baking',nutritional_information='gives you a healthy body')
# print (recipe1.recipe())

# class  MoroccanRecipe(Recipe):
#     def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information,taste,name):
#         super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
#         self.taste=taste
#         self.name=name

#     def eat_moroccan_food(self):
#         return f"The Moroccan recipe called {self.name}. It has a {self.taste} taste and contains the following ingredients: {(self.ingredients)}. It takes {self.preparation_time} to prepare and is cooked by {self.cooking_method}. It provides {self.nutritional_information}"

# moroccan_recipe = MoroccanRecipe(ingredients=["potatoes", "carrots", "onions", "garlic"], preparation_time="55 minutes", cooking_method="boiling", nutritional_information="boosts the immune system", taste="sweet", name="vegetable tagine")
# print (moroccan_recipe. eat_moroccan_food())


# class  EthiopianRecipe(Recipe):
#     def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information,spice_level,name):
#         super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
#         self.spice_level=spice_level
#         self.name=name

#     def eat_ethiopian_food(self):
#         return f"The Moroccan recipe called {self.name}. It has a {self.taste} taste and contains the following ingredients: {(self.ingredients)}. It takes {self.preparation_time} to prepare and is cooked by {self.cooking_method}. It provides {self.nutritional_information}."

# ethiopian_recipe = EthiopianRecipe(ingredients=["Whole", "wheat", "corn flour", "baking powder", "sugar", "dry yeast"], preparation_time="45 minutes", cooking_method="baked", nutritional_information="boosts the immune system", tpice_level="low", name="injera")
# print (ethiopian_recipe. eat_ethiopian_food())




# class NigerianRecipe(Recipe):
#     def __init__(self,ingredients, preparation_time, cooking_method, nutritional_information,type,name):
#         super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
#         self.type=type
#         self.name=name

#     def eat_nigerian_food(self):
#         return f"The Moroccan recipe called {self.name}. It has a {self.taste} taste and contains the following ingredients: {(self.ingredients)}. It takes {self.preparation_time} to prepare and is cooked by {self.cooking_method}. It provides {self.nutritional_information}."

# nigerian_recipe = NigerianRecipe(ingredients=["meat", "seafood", "fermented beans", "onions","vegetables"], preparation_time="30 minutes", cooking_method="boiling", nutritional_information="healthy bones", type="soup", name="egusi soup")
# print (nigerian_recipe. eat_nigerian_food())





class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method

    def display_recipe(self):
        print("Recipe Name:", self.name)
        print("Country:", self.country)
        print("Ingredients:", ', '.join(self.ingredients))
        print("Preparation Time:", self.preparation_time)
        print("Cooking Method:", self.cooking_method)


class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, spice_level):
        super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method)
        self.spice_level = spice_level

    def display_recipe(self):
        super().display_recipe()
        print("Spice Level:", self.spice_level)


class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, injera_required):
        super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method)
        self.injera_required = injera_required

    def display_recipe(self):
        super().display_recipe()
        print("Injera Required:", self.injera_required)


class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, palm_oil_used):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method)
        self.palm_oil_used = palm_oil_used

    def display_recipe(self):
        super().display_recipe()
        print("Palm Oil Used:", self.palm_oil_used)



moroccan_recipe = MoroccanRecipe("Tagine", ["Chicken", "Onion", "Spices"], 60, "Stewing", "Medium")
ethiopian_recipe = EthiopianRecipe("Doro Wat", ["Chicken", "Berbere", "Onion"], 90, "Simmering", True)
nigerian_recipe = NigerianRecipe("Jollof Rice", ["Rice", "Tomatoes", "Pepper"], 45, "Stir-frying", True)

moroccan_recipe.display_recipe()
print()
ethiopian_recipe.display_recipe()
print()
nigerian_recipe.display_recipe()



class Artist:
    def __init__(self, country, name, instruments):
        self.country = country
        self.name = name
        self.instruments = instruments
class Performance(Artist):
    def __init__(self, festival_lineup, schedule, band):
        super().__init__(festival_lineup.country, festival_lineup.name, festival_lineup.instruments)
        self.festival_lineup = festival_lineup
        self.schedule = schedule
        self.band = band
class Stage:
    def __init__(self, stage_arrangements, place, audience):
        self.stage_arrangements = stage_arrangements
        self.place = place
        self.audience = audience
artist1 = Artist("Nigeria", "Ipupa", ["guitar", "drums"])
artist2 = Artist("Cameroon", "Tryann", ["piano", "violin"])
artist3 = Artist("Kenya", "Gengetone", ["flute", "harp"])
performance1 = Performance(artist1, "Saturday, 10pm", "The Ipupa  Band")
performance2 = Performance(artist2, "Thursaday, 8pm", "The Cameroonian Tryann")
performance3 = Performance(artist3, "Wednesday, 6pm", "The Gengetone Trio")
stage1 = Stage("Open-air stage", "WaterFront Karen", 10000)
stage2 = Stage("Indoor stage", "The Concert Hall", 5000)

# Print the festival lineup
print("The festival lineup is:")
for performance in [performance1, performance2, performance3]:
    print(performance.festival_lineup.__dict__)
# Print the schedule
print("\nThe schedule is:")
for performance in [performance1, performance2, performance3]:
    print(performance.schedule)
# Print the stages
print("The stages are:")
for stage in [stage1, stage2]:
    print(stage.stage_arrangements)
# class Artist:
#     def __init__(self, name, country, musical_style, instruments):
#         self.name = name
#         self.country = country
#         self.musical_style = musical_style
#         self.instruments = instruments
#     def identify_Artist(self):
#       return f"name:{self.name} ,country:{self.country}, musical_style:{self.musical_style},instrument:{self.instruments}"
    
# artist1 = Artist("Fireboy","Nigeria","Amapiano","Guitars")    
# print(artist1.identify_Artist())


# class Performance(Artist):
  
#     def __init__(self, name, country, musical_style, instruments,start_time,end_time):
#         super().__init__(name, country, musical_style, instruments)
#         self.start_time = start_time
#         self.end_time = end_time
        
        
#     def  artist_perform(self):
#       return f"{self.name}  wil perform from {self.start_time} till {self.end_time}"

        
# performance1 = Performance("Artist1","Kenya","Amapiano","Guitar","6pm","8pm")
# print(performance1.artist_perform())
# performance2 = Performance("artist2","Nigeria","Dancing","Piano" "20:00", "21:30")


# class Stage(Artist):
#       def __init__(self, name, country, musical_style, instruments,capacity,location):
#          super().__init__(name, country, musical_style, instruments)
#          self.capacity = capacity
#          self.location = location
  
#       def add_performance(self, performance):
#         self.schedule.append(performance)
        
# stage1 = Stage("Main Stage","South Africa","Jumping","Violin","100")
# print(stage1.add_performance("dance"))

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity

# objects of the Product class
product1 = Product("Banana", 100, 10)
print(product1.calculate_total_value())

product2 = Product("Apple", 10, 5)
print(product2.calculate_total_value())

product3 = Product("Watermelom", 50, 3)
print(product3.calculate_total_value())
# total_value1 = product1.calculate_total_value()
# print(f"The total value of {product1.name} is ${total_value1}")

# product2 = Product("Watermelon", 50, 20)
# product3 = Product("kIWI", 70, 15)


# total_value1 = product1.calculate_total_value()
# total_value2 = product2.calculate_total_value()
# total_value3 = product3.calculate_total_value()


# print(f"The total value of {product2.name}s is ${total_value2}")
# print(f"The total value of {product3.name}s is ${total_value3}")



# stage2 = Stage("Acoustic Stage")  


# stage1.add_performance(performance1)
# stage2.add_performance(performance2)                
     


    
    
# class StoryTeller: 
#     def __init__(self,name, language):
#       self.name = name
#       self.language = language
    
  
#     def tellStory(story):
#       return f"Hello, I am {self.name} and my story for toaday will be from {self.language}"
  
  
#   Implement a class called Student with attributes for name, age, and grades (a
#     list of integers). Include methods to calculate the average grade, display the
#     student information, and determine if the student has passed (average grade >=
#     60). Create objects for the Student class and demonstrate the usage of these
#     methods.

# class Student:
#     def __init__(self,name,age,grades):
#         self.name =  name
#         self.age = age
#         self.grades = grades
        
 
            
       
      
      


