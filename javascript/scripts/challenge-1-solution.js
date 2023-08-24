function calculateTip(billAmount) {
    if (billAmount >= 50 && billAmount <= 300) {
        tipPercentage = 15;
} else {
    tipPercentage = 20;
}
tipAmount = billAmount * tipPercentage / 100;
totalAmount = billAmount + tipAmount;
return `The bill amount is ${billAmount} and the total amount is ${totalAmount}`;
}
console.log(calculateTip(275));
console.log(calculateTip(48));
console.log(calculateTip(430)); 