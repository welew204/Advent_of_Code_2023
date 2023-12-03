const puzzle_data = fetch("https://adventofcode.com/2023/day/2/input")
  .then((data) => data.json())
  .then((result) => console.log(result));
