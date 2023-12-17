const fs = require("fs");

function formatString(raw_data) {
  let res = {};
  let lines = raw_data.split("\n");
  let initial_seeds = [];
  let current_map = "";
  for (let i = 0; i < lines.length; i++) {
    if (i === 0) {
      let temp = lines.at(i).split(": ")[1];
      temp.split(" ").forEach((element) => {
        initial_seeds.push(parseInt(element));
      });
      res["seeds"] = initial_seeds;
      continue;
    }
    let line = lines.at(i);
    if (!line) {
      continue;
    }
    let first_character_code = line.at(0).charCodeAt(0);
    if (first_character_code > 58) {
      //this means it's text, not a digit
      let map_name = line.split(" ")[0];
      current_map = map_name;
      res[map_name] = [];
    } else {
      let ranges = line.split(" ").map((el) => parseInt(el));
      //console.log(ranges);
      res[current_map].push(ranges);
    }
  }
  return res;
}

function formatString_wrong(raw_data) {
  let res = {};
  let lines = raw_data.split("\n");
  let initial_seeds = [];
  let current_map = "";
  for (let i = 0; i < lines.length; i++) {
    if (i === 0) {
      let temp = lines.at(i).split(": ")[1];
      temp.split(" ").forEach((element) => {
        initial_seeds.push(parseInt(element));
      });
      res["seeds"] = initial_seeds;
      continue;
    }
    let line = lines.at(i);
    if (!line) {
      continue;
    }
    let first_character_code = line.at(0).charCodeAt(0);
    if (first_character_code > 58) {
      //this means it's text, not a digit
      let map_name = line.split(" ")[0];
      current_map = map_name;
      res[map_name] = {};
    } else {
      let ranges = line.split(" ").map((el) => parseInt(el));
      //console.log(ranges);
      const source_range = Array.from(
        { length: ranges[2] },
        (val, ind) => ranges[1] + ind
      );
      const dest_range = Array.from(
        { length: ranges[2] },
        (val, ind) => ranges[0] + ind
      );
      for (let i = 0; i < source_range.length; i++) {
        let source = source_range.at(i);
        let destination = dest_range.at(i);
        res[current_map][source] = destination;
      }
    }
  }
  return res;
}

function give_result(seed, range_array) {
  let match = false;
  let i = 0;
  while (match === false && i < range_array.length) {
    let source_interval_start = range_array.at(i).at(1);
    if (
      seed >= source_interval_start &&
      seed < source_interval_start + range_array.at(i).at(2)
    ) {
      match = true;
      break;
    } else if (i === range_array.length - 1) {
      return seed;
    }
    i++;
  }
  let diff = seed - range_array.at(i).at(1);
  let destination = range_array.at(i).at(0) + diff;
  return destination;
}

// rewrite trace/find:
// for each seed, look up to see which range the seed falls into (go line by line)
function simple_trace_find(input_map) {
  let res = Infinity;
  input_map.seeds.forEach((seed) => {
    let soil = give_result(seed, input_map["seed-to-soil"]);
    let fertilizer = give_result(soil, input_map["soil-to-fertilizer"]);
    let water = give_result(fertilizer, input_map["fertilizer-to-water"]);
    let light = give_result(water, input_map["water-to-light"]);
    let temp = give_result(light, input_map["light-to-temperature"]);
    let humidity = give_result(temp, input_map["temperature-to-humidity"]);
    let location = give_result(humidity, input_map["humidity-to-location"]);
    res = Math.min(res, location);
  });
  return res;
}

function map_ranges_trace_find(input_map) {
  /* My plan:
  - go thru seeds, grab start and end (exclusive)
  - map range-lines to ints
  - treat seeds as a queue (just pop items)
  - unpack these ints for comparison to seed start/end
  --> determine overlap-start and overlap-end
  --> if there is NOT an overlap, add the non-overlapping item 
  - then treat newSource as seeds, and iterate through next block
  */
  let seeds = input_map["seeds"]
    .map((s, idx, sds) => {
      if (idx % 2 === 0) {
        return [s, s + sds.at(idx + 1)];
      }
    })
    .filter((element) => element != undefined);
  let blocks = [
    input_map["seed-to-soil"],
    input_map["fertilizer-to-water"],
    input_map["water-to-light"],
    input_map["light-to-temperature"],
    input_map["temperature-to-humidity"],
    input_map["humidity-to-location"],
  ];
  let flag;
  let newSource;
  for (let block of blocks) {
    newSource = [];
    while (seeds.length > 0) {
      flag = false;
      let [s, e] = seeds.pop();
      for (let line of block) {
        let [a, b, c] = line;
        let os = Math.max(b, s);
        let oe = Math.min(b + c, e);
        if (os < oe) {
          // so if the ranges overlap
          newSource.push([os - b + a, oe - b + a]);
          if (os > s) {
            // so the s of the range preceeds the overlap (aka, b is the os)
            // add the non-overlapping hunk back to the seeds to check shit
            seeds.push([s, os]);
          }
          if (e > oe) {
            seeds.push([oe, e]);
          }
          flag = true;
          break;
        }
      }
      if (flag == false) {
        newSource.push([s, e]);
      }
    }
    seeds = newSource;
  }
  const starts = seeds.map((item) => item.at(0));
  return Math.min(...starts);
}

function brute_force_simple_trace_find_all_seeds(input_map) {
  let res = Infinity;
  input_map.seeds.forEach((seed, i, seeds) => {
    console.log(seed);
    if (i % 2 == 0) {
      let range = seeds.at(i + 1);
      for (let i = seed; i <= seed + range; i++) {
        // Your code here
        let soil = give_result(seed, input_map["seed-to-soil"]);
        let fertilizer = give_result(soil, input_map["soil-to-fertilizer"]);
        let water = give_result(fertilizer, input_map["fertilizer-to-water"]);
        let light = give_result(water, input_map["water-to-light"]);
        let temp = give_result(light, input_map["light-to-temperature"]);
        let humidity = give_result(temp, input_map["temperature-to-humidity"]);
        let location = give_result(humidity, input_map["humidity-to-location"]);
        res = Math.min(res, location);
      }
    }
  });
  return res;
}

function trace_and_find(input_map) {
  let seeds = input_map.seeds;
  let res = Infinity;
  for (let seed of seeds) {
    let soil = give_result(seed, input_map["seed-to-soil"]);
    let fertilizer = give_result(soil, input_map["soil-to-fertilizer"]);
    let water = give_result(fertilizer, input_map["fertilizer-to-water"]);
    let light = give_result(water, input_map["water-to-light"]);
    let temp = give_result(light, input_map["light-to-temperature"]);
    let humidity = give_result(temp, input_map["temperature-to-humidity"]);
    let location = give_result(humidity, input_map["humidity-to-location"]);
    res = Math.min(res, location);
  }
  return res;
}

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

//console.log(map_ranges_trace_find(sample_output_correct));

//console.log(simple_trace_find(formatString(sample_1_string)));

fs.readFile(
  "/Users/williamhbelew/Hacking/AoC_2023/will/puzzle_inputs/d5_almanac.txt",
  "utf8",
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }

    //const puzzle_object = formatString(data);
    //console.log(map_ranges_trace_find(puzzle_object));
    return;
  }
);

module.exports.handle_string = formatString;
module.exports.find_min = simple_trace_find;
module.exports.map_ranges = map_ranges_trace_find;
