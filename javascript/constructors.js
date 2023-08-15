//WITH USING A CONSTRUCTOR
//A constructor is just a function called using the 'new' keyword
//When you call a constructor, it will create a new object, bind this to the new object, so you can refer to this in your constructor code, run the code in the constructor, return the new object
//Constructors start by capital letter
function Person(name) {
    this.name = name;
    this.introduceSelf = function () {
      console.log(`Hi! I'm ${this.name}.`);
    };
}
//To call a person, we use new
const person1 = new Person("Salva");
person1.name;
person1.introduceSelf(); //Hi! I'm Salva.

const person2 = new Person("Frankie");
person2.name;
person2.introduceSelf(); //Hi! I'm Frankie.




//WITHOUT USING A CONSTRUCTOR
// function createPerson(name) {
//   const obj = {};
//   obj.name = name;
//   obj.introduceSelf = function () {
//     console.log(`Hi! I'm ${this.name}.`);
//   };
//   return obj;
//   //This function creates and returns a new obj each time we call it
//   //Th object wil have two members, a property name and a method introduce()
// }
// //create obj
// const salva = createPerson("Salva");
// salva.name;
// salva.introduceSelf();
// //output: Hi! I'm Salva.

// const frankie = createPerson("Frankie");
// frankie.name;
// frankie.introduceSelf();
// //Hi! I'm Frankie.

let b = 1;

function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);