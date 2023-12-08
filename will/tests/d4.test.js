const d4_scratcher = require("../d4_scratchcards");

const pt_1_sample_string = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`;
const pt_1_sample_1 = [
  [
    [41, 48, 83, 86, 17],
    [83, 86, 6, 31, 17, 9, 48, 53],
  ],
  [
    [13, 32, 20, 16, 61],
    [61, 30, 68, 82, 17, 32, 24, 19],
  ],
  [
    [1, 21, 53, 59, 44],
    [69, 82, 63, 72, 16, 21, 14, 1],
  ],
  [
    [41, 92, 73, 84, 69],
    [59, 84, 76, 51, 58, 5, 54, 83],
  ],
  [
    [87, 83, 26, 28, 32],
    [88, 30, 70, 12, 93, 22, 82, 36],
  ],
  [
    [31, 18, 13, 56, 72],
    [74, 77, 10, 23, 35, 67, 36, 11],
  ],
];

const pt2_sample_string = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`;

test("checking string handling...", () => {
  expect(d4_scratcher.handle_string(pt_1_sample_string)).toStrictEqual(
    pt_1_sample_1
  );
});

test("First test case...", () => {
  expect(d4_scratcher.calc_sum(pt_1_sample_1)).toBe(13);
});

test("Second test case ...", () => {
  expect(
    d4_scratcher.calc_total_cards(d4_scratcher.handle_string(pt2_sample_string))
  ).toBe(30);
});
