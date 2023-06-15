// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

// pseudo code
// input    length of the story     
            // moral lessons
            //agegroup

// output     storytelling

// process      create classes-StoryTelling
                // constructor


class Story {
    constructor(title, moralLesson, length, ageGroup) {
      this.title = title;
      this.moralLesson = moralLesson;
      this.length = length;
      this.ageGroup = ageGroup;
    }
  
   
    display() {
      console.log(`Title: ${this.title}`);
      console.log(`Content: ${this.moralLesson}`);
      console.log(`Length: ${this.length}`);
      console.log(`Age Group: ${this.ageGroup}`);
    }
  }
  
 
  class StoryTeller {
    constructor(name) {
      this.name = name;
    }
  
    
    tellStory(story) {
      console.log(`${this.name} will tell a story`);
      story.display();
    }
  }
  
 

  
 
  const story = new Story(
    "The Lion and the Hare",
    "Once upon a time...",
    "Medium",
    "Children"
  );

  
  story.display();

  



// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.




class Recipe{
    constructor(ingeredients,preparationTime, cookingMethod, nutritionalInformation){
        this.ingeredients = ingeredients
        this.preparationTime = preparationTime
        this.cookingMethod = cookingMethod
        this.nutritionalInformation = nutritionalInformation

    }

    // differentRecipes(){
    //     return(`${this.constructor.name} ${this.ingeredients}`)
    // }
    
}


class MoroccanRecipe extends Recipe{
    // constructor(ingeredients,preparationTime,cookingMethod,nutritionalInformation){
    //     super(ingeredients,preparationTime,cookingMethod,nutritionalInformation)


    // }
    prepareFood(){
        return `Moroccan food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
    }
    
    

}

class EthiopianRecipe extends Recipe{
    prepareEthiopanDish(){
        return `Ethiopian food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
    }

}

class NigerianRecipe extends Recipe{
    prepareNigerFood(){
        return `Nigeria food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
    }

}

const recipe = new MoroccanRecipe("pepper","one hour", "Boilin water","keeps the body fit")
console.log(recipe.prepareFood);

const recipes = new EthiopianRecipe("Cumin","two hour", "stew","keeps the body fit")
console.log(recipe.EthiopianRecipe());

const foods = new NigerianRecipe("pepper"," 0n3 hour", "fufu","keeps the body fit")
console.log(recipe.NigerianRecipe());


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.


// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product{
    constructor(name,price,quantity){
        this.name = name
        this.price = price
        this.quantity = quantity
    }

    calculateTotalValue(){

    }

}


// Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.


class Student {
  constructor(name, age, grades) {
    this.name = name;
    this.age = age;
    this.grades = grades;
  }

  calculateAverageGrade() {
    if (this.grades.length === 0) {
      return 0;
    }
    const sum = this.grades.reduce((total, grade) => total + grade);
    return sum / this.grades.length;
  }

  studentsdetails() {
    console.log(`Name: ${this.name}`);
    console.log(`Age: ${this.age}`);
    console.log(`Grades: ${this.grades.join(', ')}`);
    console.log(` The Average Grade: ${this.calculateAverageGrade()}`);
  }

  ifPassed() {
    return this.calculateAverageGrade() >= 60;
  }
}


const student1 = new Student('Mary', 16, [30,40,60]);
const student2 = new Student('Peter', 14, [45,60,70]);
const student3 = new Student('Tina', 17, [30,70,90]);


student1.studentsdetails();
console.log('pass:', student1.ifPassed());

student2.displayStudentInfo();
console.log('pass:', student2.ifPassed());

student3.displayStudentInfo();
console.log('pass:', student3.ifPassed());


// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

class FlightBooking{
    constructor(destination, date,reservedSeats,passangerInformation, bookingConfirmation){

    }
}
                


