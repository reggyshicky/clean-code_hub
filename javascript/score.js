// Calculate the average score for a team
function calculateAverage(scores) {
  const total = scores.reduce((sum, score) => sum + score, 0);
  return total / scores.length;
}

// Determine the winner or draw between two teams
function determineWinnerOrDraw(team1, team2) {
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
const manuTestData1 = [96, 108, 89];
const arsenalTestData1 = [88, 91, 110];

const manuTestData2 = [97, 112, 101];
const arsenalTestData2 = [109, 95, 123];

// Determine the winner or draw for each test data set
console.log("Test Data 1:");
console.log("Winner:", determineWinnerOrDraw(manuTestData1, arsenalTestData1));

console.log("\nTest Data 2:");
console.log("Winner:", determineWinnerOrDraw(manuTestData2, arsenalTestData2));
