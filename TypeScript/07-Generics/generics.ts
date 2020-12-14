function pickNumber(numbers: number[]): number{
    const randomIndex = Math.floor(Math.random() * numbers.length);
    return numbers[randomIndex];
}

const numbers = [...Array(13).keys()];
const pickedNumber = pickNumber(numbers);
console.log(pickedNumber);

function pickSuit(suits: string[]): string{
    const randomIndex = Math.floor(Math.random() * suits.length);
    return suits[randomIndex];
}

const suits = ['diamonds', 'clubs', 'hearts', 'spades'];
const pickedSuit = pickSuit(suits);
console.log(pickedSuit);


/***********************************************************
 * Generic
***********************************************************/
function genericPicker<T>(args: T[]): T {
    const randomIndex = Math.floor(Math.random() * args.length);
    return args[randomIndex];
}

console.log(genericPicker(suits), genericPicker(numbers));