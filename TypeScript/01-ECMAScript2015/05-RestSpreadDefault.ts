/***********************************************************
 * Rest, Spread, and Defaults Intro
 ***********************************************************/
function add1(...numbers) {
    return numbers.reduce(function(acc, number) {
        return acc + number;
    });
};

console.log(add1(3,4,6));
//[LOG]: 13


/***********************************************************
* Add function that is type aware and has an arrow function
***********************************************************/
function add(...numbers: Array<number>) {
    return numbers.reduce((acc, number) => acc + number);
};

console.log(add(3,4,6));
//[LOG]: 13

/***********************************************************
 * Add two arrays together
 ***********************************************************/
const fruit: Array<String> = ['apple', 'pear'];
const moreFruit: Array<String> = ['peach'];

//Use spread operator to concat!
const allFruit: Array<String> = [...fruit, ...moreFruit];
console.log(allFruit);
//[LOG]: ["apple", "pear", "peach"]

/***********************************************************
 * Default Parameters
 ***********************************************************/

//Classic
function multiply1(num: number, multiplier: number){
    num = (num !== undefined) ? num : 0;
    multiplier = (multiplier !== undefined) ? multiplier : 1;
    return num * multiplier;
};

console.log(
    multiply1()
    ,multiply1(5)
    ,multiply1(5, 2)
);
//[LOG]: 0,  5,  10

//ECMA 2015
function multiply2(num: number = 0, multiplier: number = 1){
    return num * multiplier;
};

console.log(
    multiply2()
    ,multiply2(5)
    ,multiply2(5, 2)
);
//[LOG]: 0,  5,  10

//ECMA 2015 + Arrow Function
const multiply = (num: number = 0, multiplier: number = 1) => (num * multiplier);

console.log(
    multiply()
    ,multiply(5)
    ,multiply(5, 2)
);
//[LOG]: 0,  5,  10