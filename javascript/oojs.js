const person = {
  name: ["Bob", "Smith"],
  age: 32,
};
const myDataName = "height";
const myDataValue = "1.75m";
person[myDataName] = myDataValue; 
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


