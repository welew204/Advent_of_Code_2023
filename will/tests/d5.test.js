const d5_almanac = require("../d5_almanac");

sample_1_string = `seeds: 79 14 55 13
seed-to-soil map:
50 98 2
52 50 48
soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15
fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4
water-to-light map:
88 18 7
18 25 70
light-to-temperature map:
45 77 23
81 45 19
68 64 13
temperature-to-humidity map:
0 69 1
1 0 69
humidity-to-location map:
60 56 37
56 93 4`;

const sample_output_correct = {
  seeds: [79, 14, 55, 13],
  "seed-to-soil": [
    [50, 98, 2],
    [52, 50, 48],
  ],
  "soil-to-fertilizer": [
    [0, 15, 37],
    [37, 52, 2],
    [39, 0, 15],
  ],
  "fertilizer-to-water": [
    [49, 53, 8],
    [0, 11, 42],
    [42, 0, 7],
    [57, 7, 4],
  ],
  "water-to-light": [
    [88, 18, 7],
    [18, 25, 70],
  ],
  "light-to-temperature": [
    [45, 77, 23],
    [81, 45, 19],
    [68, 64, 13],
  ],
  "temperature-to-humidity": [
    [0, 69, 1],
    [1, 0, 69],
  ],
  "humidity-to-location": [
    [60, 56, 37],
    [56, 93, 4],
  ],
};

test("D5: checking string handling...", () => {
  expect(d5_almanac.handle_string(sample_1_string)).toStrictEqual(
    sample_output_correct
  );
});

test("D5: testing pt 1 functionality...", () => {
  expect(d5_almanac.find_min(sample_output_correct)).toBe(35);
});
