const http = require("node:http");
const hostname = "127.0.0.1";
const port = 3000;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("No waaayyy YA!\n");
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

const fs = require("fs");

fs.readFile(
  "/Users/williamhbelew/Hacking/AoC_2023/puzzle_inputs/d3_engineSchematic.txt",
  "utf8",
  (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    // Split the data into lines
    let lines = data.split("\n");
    //console.log(lines);

    let asciiPunctuationSymbols = [];
    const ranges = [
      [33, 46],
      [47, 48],
      [58, 65],
      [91, 97],
      [123, 127],
    ];

    ranges.forEach(([start, end]) => {
      for (let i = start; i < end; i++) {
        asciiPunctuationSymbols.push(i);
      }
    });
    //console.log(asciiPunctuationSymbols);
    let symbol_index = [];
    let row_length;

    for (let i = 0; i < lines.length; i++) {
      let row = lines.at(i);
      //console.log(row);
      if (i === 0) {
        row_length = row.length;
      }
      for (let j = 0; j < row.length; j++) {
        let char = row.charCodeAt(j);
        //console.log(char);
        // previeous......
        // if (asciiPunctuationSymbols.includes(char)) {
        if (char === 42) {
          // now only chekc foring '*' gears
          symbol_index.push([i, j]);
        }
      }
    }
    //console.log(symbol_index);
    function isDigit(char) {
      return !isNaN(parseInt(char)) && isFinite(char);
    }
    let engine_schematics = [];
    let visited = new Set();

    for (let tup of symbol_index) {
      //console.log(tup);
      let [i, j] = tup;
      let checkr_res = [];
      visited.add(`${i},${j}`);
      let i_range = [i - 1, i, i + 1];
      let j_range = [j - 1, j, j + 1];
      for (let i_coord of i_range) {
        for (let j_coord of j_range) {
          if (
            visited.has(`${i_coord},${j_coord}`) === false &&
            i_coord >= 0 &&
            j_coord >= 0 &&
            i_coord < lines.length &&
            j_coord < row_length
          ) {
            visited.add(`${i_coord},${j_coord}`);
            let target = lines.at(i_coord).at(j_coord);
            if (
              target != "." &&
              asciiPunctuationSymbols.includes(target.charCodeAt(0)) === false
            ) {
              //console.log(target);
              //console.log("Is this a symbol? ^^");
              let [l, r] = [j_coord - 1, j_coord + 1];
              let result = target;
              while (l >= 0 && isDigit(lines.at(i_coord).at(l))) {
                let d = lines.at(i_coord).at(l);
                result = d + result;
                visited.add(`${i_coord},${l}`);
                l--;
              }
              while (r < row_length && isDigit(lines.at(i_coord).at(r))) {
                let d = lines.at(i_coord).at(r);
                result += d;
                visited.add(`${i_coord},${r}`);
                r++;
              }
              //console.log(result);
              checkr_res.push(parseInt(result));
            }
          }
        }
      }
      if (checkr_res.length === 2) {
        // EXACTLY two numbers....
        let gear_ratio = checkr_res[0] * checkr_res[1];
        engine_schematics.push(gear_ratio);
      }
    }
    let sum = engine_schematics.reduce((acc, curr) => acc + curr);
    console.log(sum);
    /* 
    // Process each line and split it into elements
    let array = lines.map((line) => line.trim().split(",")); // Change ',' to your delimiter

  // Adjusting the array to fit [i, j] dimensions
  const i = 4; // desired number of rows
  const j = 3; // desired number of columns

  array = array.slice(0, i).map((row) => row.slice(0, j));

  // Handling cases where rows or columns are fewer than desired
  while (array.length < i) {
    array.push(new Array(j).fill(null)); // Fill with null or any default value
  }

  array = array.map((row) => {
    while (row.length < j) {
      row.push(null); // Again, fill with null or any default value
    }
    return row;
  });

  console.log(array); */
  }
);
