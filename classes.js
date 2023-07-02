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


class OralStories{
    constructor(title,storyLength,moralLesson){
    this.title=title
    this.storyLength=storyLength
    this.moralLesson=moralLesson
    }

}
let story1=new OralStories("The Hare and the hyena",500 ,["being clever","making wise decions"])
let story2=new OralStories("The Baby Chick",400 ,["being clever","caring about others"])
console.log(story1);
console.log(story2);


class StoryTeller extends OralStories{
    constructor(name,title){
    super(title)
    this.name=name
  
    }
    tellStories(){
        console.log(`The story ${title} was narrated by ${this.name}`);
    }
}
let storyteller=new StoryTeller("Mercy","The flying bird")
console.log(storyteller);


class  Translator extends OralStories{
    constructor(translatorName,title,language,storyLength,moralLesson){
        super(title,storyLength,moralLesson)
        this.translatorName=translatorName
        this.language=language
    }
    get_translation(){
        console.log(`The story ${this.title} is narrated in ${this.language} and is translated by ${this.translatorName}. It's ${this.storyLength} and has it enlightens people to ${this.moralLesson}`)
    }
}
let translator=new Translator("Mary","The Birds of the mountain","Kiswahili","medium","take caution")
console.log(translator.get_translation());


class Recipe{
    constructor(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName){
        this.uniqueIngrdients=uniqueIngrdients
        this.preparationTime=preparationTime
        this.cookingMethod=cookingMethod
        this.nutritionalInfaormation=nutritionalInformation
        this.foodName=foodName
    }
    recipeRequirements(){
        return `some foods use  ${this.uniqueIngrdients} which is prepared ${this.preparationTime} using ${this.cookingMethod} and has ${this.nutritionalInfaormation}`
    }
}
let recipes= new Recipe("simple ingredients","1hr 30min","easy","good health","Africa food")
console.log(recipes.recipeRequirements());
console.log(recipes);

class MoroccanRecipe extends Recipe{
    constructor(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,lotOfSpice,foodName){
        super(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName)
        this.lotOfSpice=lotOfSpice
    }
    eatMorrocan(){
 return `Every ${this.foodName} has ${this.lotOfSpice}`
    }     
}
let morrocan =new MoroccanRecipe ("olive oil","1hr","frying","strong body","seafood","enough spice")
console.log(morrocan.eatMorrocan());

class EthiopianRecipe extends Recipe{
    constructor(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName,lotOfPepper){
        super(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName)  
        this.lotOfPepper=lotOfPepper
    }
    eatEthiopian(){
        return `Every ${this.foodName} has ${this.lotOfPepper}`
    }
   
}
let eathiopian=new EthiopianRecipe ("yam floor","1hr","boiling","strong body","injera","enough spice")
console.log(eathiopian.eatEthiopian());

class NigerianRecipe extends Recipe{
    constructor(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName,garri){
        super(uniqueIngrdients,preparationTime,cookingMethod,nutritionalInformation,foodName)
        this.garri=garri
    }
    eatNigerian(){
        return `Every ${this.foodName} has ${this.garri}`
    }
}
let nigerian =new NigerianRecipe ("salt","2hr","deep frying","maintainance","jollof","enough turkey")
console.log(nigerian.eatNigerian());


class Product{
    constructor(name,price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }
    totalValue(){
        return  this.price * this.quantity
    }
}
let product=new Product('milk',20,3)
console.log(product.totalValue());














class Student {
    constructor(name, age, grades) {
      this.name = name;
      this.age = age;
      this.grades = grades;
    }
  
    calculateAverageGrade() {
      let sum = 0;
      for (let i = 0; i < this.grades.length; i++) {
        sum += this.grades[i];
      }
      return sum / this.grades.length;
    }
  
    displayStudentInfo() {
      console.log(`Name: ${this.name}`);
      console.log(`Age: ${this.age}`);
      console.log(`Grades: ${this.grades.join(", ")}`);
    }
  
    hasPassed() {
      return this.calculateAverageGrade() >= 60;
    }
  }
  
  // Creating objects for the Student class and demonstrating the usage of methods
  
  const student1 = new Student("John Doe", 18, [80, 75, 90, 85]);
  student1.displayStudentInfo();
  console.log(`Average Grade: ${student1.calculateAverageGrade()}`);
  console.log(`Has Passed: ${student1.hasPassed()}`);
  
  const student2 = new Student("Jane Smith", 20, [70, 65, 80, 75]);
  student2.displayStudentInfo();
  console.log(`Average Grade: ${student2.calculateAverageGrade()}`);
  console.log(`Has Passed: ${student2.hasPassed()}`);


// class Story {
//     constructor(title, moralLesson, length, ageGroup) {
//       this.title = title;
//       this.moralLesson = moralLesson;
//       this.length = length;
//       this.ageGroup = ageGroup;
//     }
  
   
  //   display() {
  //     console.log(`Title: ${this.title}`);
  //     console.log(`Content: ${this.moralLesson}`);
  //     console.log(`Length: ${this.length}`);
  //     console.log(`Age Group: ${this.ageGroup}`);
  //   }
  // }
  
 
  // class StoryTeller {
  //   constructor(name) {
  //     this.name = name;
  //   }
  
    
  //   tellStory(story) {
  //     console.log(`${this.name} will tell a story`);
  //     story.display();
  //   }
  // }
  
 

  
 
  // const story = new Story(
  //   "The Lion and the Hare",
  //   "Once upon a time...",
  //   "Medium",
  //   "Children"
  // );

  
  // story.display();

  



// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.




// class Recipe{
//     constructor(ingeredients,preparationTime, cookingMethod, nutritionalInformation){
//         this.ingeredients = ingeredients
//         this.preparationTime = preparationTime
//         this.cookingMethod = cookingMethod
//         this.nutritionalInformation = nutritionalInformation

//     }

    // differentRecipes(){
    //     return(`${this.constructor.name} ${this.ingeredients}`)
    // }
    
// }


// class MoroccanRecipe extends Recipe{
    // constructor(ingeredients,preparationTime,cookingMethod,nutritionalInformation){
    //     super(ingeredients,preparationTime,cookingMethod,nutritionalInformation)


    // }
//     prepareFood(){
//         return `Moroccan food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
//     }
    
    

// }

// class EthiopianRecipe extends Recipe{
//     prepareEthiopanDish(){
//         return `Ethiopian food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
//     }

// }

// class NigerianRecipe extends Recipe{
//     prepareNigerFood(){
//         return `Nigeria food is prepared using ${this.ingeredients} .The allocated time is${this.preparationTime}, and the ${this.cookingMethod} as the expertise says it has  ${this.nutritionalInformation}`
//     }

// }

// const recipe = new MoroccanRecipe("pepper","one hour", "Boilin water","keeps the body fit")
// console.log(recipe.prepareFood);

// const recipes = new EthiopianRecipe("Cumin","two hour", "stew","keeps the body fit")
// console.log(recipes.EthiopianRecipe());

// const foods = new NigerianRecipe("pepper"," 0n3 hour", "fufu","keeps the body fit")
// console.log(foods.NigerianRecipe());


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.


// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

// class Product{
//     constructor(name,price,quantity){
//         this.name = name
//         this.price = price
//         this.quantity = quantity
//     }

//     calculateTotalValue(){

//     }

// }


// Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.


// class Student {
//   constructor(name, age, grades) {
//     this.name = name;
//     this.age = age;
//     this.grades = grades;
//   }

//   calculateAverageGrade() {
//     if (this.grades.length === 0) {
//       return 0;
//     }
//     const sum = this.grades.reduce((total, grade) => total + grade);
//     return sum / this.grades.length;
//   }

//   studentsdetails() {
//     console.log(`Name: ${this.name}`);
//     console.log(`Age: ${this.age}`);
//     console.log(`Grades: ${this.grades.join(', ')}`);
//     console.log(` The Average Grade: ${this.calculateAverageGrade()}`);
//   }

//   ifPassed() {
//     return this.calculateAverageGrade() >= 60;
//   }
// }


// const student1 = new Student('Mary', 16, [30,40,60]);
// const student2 = new Student('Peter', 14, [45,60,70]);
// const student3 = new Student('Tina', 17, [30,70,90]);


// student1.studentsdetails();
// console.log('pass:', student1.ifPassed());

// student2.displayStudentInfo();
// console.log('pass:', student2.ifPassed());

// student3.displayStudentInfo();
// console.log('pass:', student3.ifPassed());


// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

// class FlightBooking{
//     constructor(destination, date,reservedSeats,passangerInformation, bookingConfirmation){

//     }
// }
                


