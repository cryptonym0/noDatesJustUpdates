const numbers1: number[] = [0, 1, 2, 3];

const greaterThanTwo: number[] =
    numbers1.filter(number => number > 2);

console.log(greaterThanTwo);

// tsc --target es6 first.ts
//to run
//node first.js
//or
//ts-node first.ts 