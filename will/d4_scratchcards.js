const fs = require("fs");

const pt_1_sample_string = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`;

let puzzle_input = [];
fs.readFile(
  "/Users/williamhbelew/Hacking/AoC_2023/will/puzzle_inputs/d4_scratchers.txt",
  "utf8",
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }

    puzzle_input = handle_input(data);
    //console.log(d4_scratcher_pt_1(puzzle_input));
    console.log(d4_scratcher_pt_2(puzzle_input));
    return;
  }
);

function handle_input(raw_data) {
  let res = [];
  let lines = raw_data.split("\n");
  for (let line of lines) {
    line = line.split(": ")[1];
    line = line.split(" | ");
    let winning_nums = [];
    let cards_nums = [];
    for (let num of line[0].split(" ")) {
      if (num !== "") {
        winning_nums.push(parseInt(num));
      }
    }
    for (let num of line[1].split(" ")) {
      if (num !== "") {
        cards_nums.push(parseInt(num));
      }
    }
    //console.log([winning_nums, cards_nums]);
    res.push([winning_nums, cards_nums]);
  }
  return res;
}

function d4_scratcher_pt_1(puzzle_input) {
  // turn winning-nums into a set, for fast checking
  // iterate thru cards, tally num of hits
  // if hits > 0, return 2**(num_hits-1)
  result = 0;
  for (let card of puzzle_input) {
    let winners = new Set(card[0]);
    let nums = card[1];
    let resulting_points = 0;
    let hits = determine_winners(winners, nums);
    if (hits > 0) {
      resulting_points = 2 ** (hits - 1);
    }
    result += resulting_points;
  }
  return result;
}

function determine_winners(winning_set, candidates) {
  let hits = 0;
  for (let n of candidates) {
    if (winning_set.has(n)) {
      hits += 1;
    }
  }
  return hits;
}

function d4_scratcher_pt_2(cards) {
  let card_map = {};
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    let winners = new Set(card[0]);
    let nums = card[1];
    let resulting_points = 0;
    let hits = determine_winners(winners, nums);
    card_map[i + 1] = { hits: hits, copies: 1 };
  }
  Object.entries(card_map).forEach(([k, v]) => {
    //console.log(k, v);
    for (let i = 1; i <= v.hits; i++) {
      //console.log(card_map[parseInt(k)].copies);
      let to_add = card_map[parseInt(k)].copies;
      card_map[parseInt(k) + i].copies += to_add;
    }
  });
  let result_sum = 0;
  Object.entries(card_map).forEach(([k, v]) => {
    result_sum += v.copies;
  });

  return result_sum;
}
// TODO: D4_scratcher_pt2: build a hashmap keyed on the day; first pass find number of winners, count each as 1;
// then go back through, and tally number of copies based on down-tracking the wins

handle_input(pt_1_sample_string);
const pt2_sample_string = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`;
console.log(d4_scratcher_pt_2(handle_input(pt2_sample_string)));

module.exports.calc_sum = d4_scratcher_pt_1;
module.exports.calc_total_cards = d4_scratcher_pt_2;
module.exports.handle_string = handle_input;
