const d6_raceOpt = require("../d6_raceOpt");

const d6_sampleString = `Time:      7  15   30
Distance:  9  40  200`;

//console.log(d6_raceOpt.formatString(d6_sampleString));

const sample_correct_output = { times: [7, 15, 30], distances: [9, 40, 200] };
const pt2_sample_correct_output = { times: [71530], distances: [940200] };

test("D6, pt1: formatting string...", () => {
  expect(d6_raceOpt.formatString(d6_sampleString)).toStrictEqual(
    sample_correct_output
  );
});

test("D6, pt2: formatting string...", () => {
  expect(d6_raceOpt.formatString_pt2(d6_sampleString)).toStrictEqual(
    pt2_sample_correct_output
  );
});

test("D6, pt 1: checking winning paths, returning factored result.", () => {
  expect(d6_raceOpt.calcWinningTimings(sample_correct_output)).toBe(288);
});

test("D6, pt 2: checking winning paths, returning factored result.", () => {
  expect(d6_raceOpt.calcWinningTimings_pt2(pt2_sample_correct_output)).toBe(
    71503
  );
});
