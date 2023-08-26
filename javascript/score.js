// Calculate the average score for a team
const calculateAverage = scores => {
  let total = 0;
  for (const score of scores) {
    total += score;
  }
  return total / scores.length;
};

// Determine the winner or draw between two teams
const checkWinner = function(team1, team2) {
  const averageScoreTeam1 = calculateAverage(team1);
  const averageScoreTeam2 = calculateAverage(team2);

  if (averageScoreTeam1 >= 100 && averageScoreTeam2 >= 100) {
    if (averageScoreTeam1 > averageScoreTeam2) {
      return "Manu";
    } else if (averageScoreTeam2 > averageScoreTeam1) {
      return "Arsenal";
    } else {
      return "Draw";
    }
  } else {
    return "No winner due to insufficient scores";
  }
}
//averageScoreTeam1 >= 100 && averageScoreTeam2 >= 100
// ? averageScoreTeam1 > averageScoreTeam2
//    : 
const manuTestData1 = [44, 23, 71];
const arsenalTestData1 = [ 85, 54, 41];

const manuTestData2 = [85, 54, 41];
const arsenalTestData2 = [23, 34, 27];

// Determine the winner or draw for each test data set
console.log("Test Data 1:");
console.log("Winner:", checkWinner(manuTestData1, arsenalTestData1));

console.log("\nTest Data 2:");
console.log("Winner:", checkWinner(manuTestData2, arsenalTestData2));
