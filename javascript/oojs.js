const person = {
  name: ["Bob", "Smith"],
  age: 32,
};
const myDataName = "height";
const myDataValue = "1.75m";
person[myDataName] = myDataValue; 
//Adding a property to an obj using the method above is not possible with dot notation, which can only accept a literal member
//not a variable value pointing to a  name
//setting object members
person.name[1] = "Reggy";
person.age = 24;
//Creating completely new members
person.food = "ricestew";
person["music"] = "popmusic";

function logproperty(propertyName) {
  console.log(person[propertyName]);
}
logproperty("name");
logproperty("age");
logproperty("food");
logproperty("music");
logproperty("height")
//output: [ 'Bob', 'Smith' ]
//32


