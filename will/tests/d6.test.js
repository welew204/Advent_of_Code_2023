const d6_raceOpt = require("../d6_raceOpt");

const d6_sampleString = `Time:      7  15   30
Distance:  9  40  200`;

//console.log(d6_raceOpt.formatString(d6_sampleString));

const sample_correct_output = { times: [7, 15, 30], distances: [9, 40, 200] };

test("D6: formatting string...", () => {
  expect(d6_raceOpt.formatString(d6_sampleString)).toStrictEqual(
    sample_correct_output
  );
});

test("D6: checking winning paths, returning factored result.", () => {
  expect(d6_raceOpt.calcWinningTimings(sample_correct_output)).toBe(288);
});
