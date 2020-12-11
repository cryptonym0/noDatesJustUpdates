/***********************************************************
 * Arrow Function Intro
 ***********************************************************/

//Classic
const numbers = [0, 1, 2];
numbers.map(function(number){
    return console.log(number);
});

//Arrow
numbers.map(number => console.log(number));

//diff
const quotient1 = {
    numbers: [1, 2, 3, 4, 5, 6, 7],
    results: [],
    divideFn: function(divisor) {
        return this.numbers.map(function (divident) {
            if (divident % divisor === 0) {
                return this.results.push(divident);
            }
        }.bind(this));
    }
};

quotient1.divideFn(3);
console.log(quotient1.results);


const quotient = {
    numbers: [1, 2, 3, 4, 5, 6, 7],
    results: [],
    divideFn: function(divisor: number) {
        return this.numbers.map(divident => {
            if (divident % divisor === 0) {
                return this.results.push(divident);
            }
        });
    }
};

quotient.divideFn(3);
console.log(quotient.results);

//more than one argument
const greet = (fname, age) => ({
    fname,
    age
});

console.log(greet('Steve', 18));
// [LOG]: {
//     "fname": "Steve",
//         "age": 18
// }