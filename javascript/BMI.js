const Dan = {
    weight: 78,
    height: 1.69
};

const Sarah = {
      weight: 87,
      height: 1.95
};

let sarah_BMI  = Sarah.weight / (Sarah.height * Sarah.height);
let Dan_BMI = Dan.weight / (Dan.height * Dan.height);

if (sarah_BMI > Dan_BMI) {
  console.log('Sarah has the bigger BMI');
} else {
    console.log('Dan has the bigger BMI');
}
