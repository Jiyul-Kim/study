const texts = ["house", "go", "sleep"];
const caps = texts.map(function (t) {
  return t.toUpperCase();
});
texts; // ['house', 'go', 'sleep']
caps; // ['HOUSE', 'GO', 'SLEEP']

const numbers = [1, 2, 3, 4, 5];
const doubles = numbers.map(function (num) {
  return num * 2;
});

// 코딩 연습 47번
const fullNames = [
  { first: "Albus", last: "Dumbledore" },
  { first: "Harry", last: "Potter" },
  { first: "Hermione", last: "Granger" },
  { first: "Ron", last: "Weasley" },
  { first: "Rubeus", last: "Hagrid" },
  { first: "Minerva", last: "McGonagall" },
  { first: "Severus", last: "Snape" },
];

const firstNames = fullNames.map(function (fistname) {
  return fistname.first;
});

