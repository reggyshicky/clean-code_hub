const myBoolean = true;
const myString = 'hello world';
const myFirstNumber = 20;
let mySecondNumber = 40;
mySecondNumber = 80

const myArray = [myBoolean, myString];
const myObject = {
    firstProperty: myArray,
    sumProperty:  parseInt(myFirstNumber) + parseInt(mySecondNumber)
};
console.log(myObject)
console.log(myObject.firstProperty[1])
console.log(myObject.sumProperty)