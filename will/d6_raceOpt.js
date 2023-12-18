const fs = require("fs");

function formatString(raw_input) {
  const lines = raw_input.split("\n");
  let res = {};
  let times = lines.at(0).split(":").at(1).split(" ");
  let trimmedTimes = times
    .filter((time) => time != "")
    .map((time) => parseInt(time));
  let distances = lines.at(1).split(": ").at(1).split(" ");
  let trimmedDistances = distances
    .filter((dist) => dist != "")
    .map((dist) => parseInt(dist));
  res.times = trimmedTimes;
  res.distances = trimmedDistances;
  return res;
}

function formatString_pt2(raw_input) {
  const lines = raw_input.split("\n");
  let res = {};
  let times = lines.at(0).split(":").at(1).split(" ");
  let trimmedTime = times
    .filter((time) => time != "")
    .reduce((prev_string, next_int) => prev_string + next_int);
  let distances = lines.at(1).split(": ").at(1).split(" ");
  let trimmedDistance = distances
    .filter((dist) => dist != "")
    .reduce((prev_string, next_int) => prev_string + next_int);
  res.times = [parseInt(trimmedTime)];
  res.distances = [parseInt(trimmedDistance)];
  return res;
}

function calcWinningTimings(inputObj) {
  /* for range of timing from 0 - timing,
  check if result beats current record, 
  if it does, increment winning-paths result int,
  when done add to final result array
  return factored list
   */
  let res = [];
  for (let i = 0; i < inputObj.times.length; i++) {
    let winning_paths = 0;
    let timeToBeat = inputObj.distances.at(i);
    for (let j = 0; j <= inputObj.times.at(i); j++) {
      // j = amt of time holding the button AND the speed of travel once released
      let timeOfTravel = inputObj.times.at(i) - j;
      let attemptDist = timeOfTravel * j;
      if (attemptDist > timeToBeat) {
        winning_paths += 1;
      }
    }
    res.push(winning_paths);
    /*     if (winning_paths > 0) {
    } */
  }
  res = res.reduce((prev, n_fact) => prev * n_fact);
  return res;
}

function calcWinningTimings_pt2(inputObj) {
  /* for range of timing from 0 - timing,
  check if result beats current record, 
  if it does, increment winning-paths result int,
  when done add to final result array
  return factored list
   */

  let winning = false;

  let winning_paths = 0;
  let timeToBeat = inputObj.distances.at(0);
  for (let j = 0; j <= inputObj.times.at(0); j++) {
    // j = amt of time holding the button AND the speed of travel once released
    let timeOfTravel = inputObj.times.at(0) - j;
    let attemptDist = timeOfTravel * j;
    if (attemptDist > timeToBeat) {
      winning_paths += 1;
      winning = true;
    } else if (winning === true) {
      /* essentially, you have now crossed over into paths that don't have enough time to execute */
      return winning_paths;
    }
  }
  return winning_paths;
}

fs.readFile(
  "/Users/williamhbelew/Hacking/AoC_2023/will/puzzle_inputs/d6_races.txt",
  "utf8",
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }

    const puzzle_object = formatString_pt2(data);
    console.log(calcWinningTimings_pt2(puzzle_object));
    return;
  }
);

module.exports.formatString = formatString;
module.exports.formatString_pt2 = formatString_pt2;
module.exports.calcWinningTimings = calcWinningTimings;
module.exports.calcWinningTimings_pt2 = calcWinningTimings_pt2;
