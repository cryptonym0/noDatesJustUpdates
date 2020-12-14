/***********************************************************
 * Arrays
 ***********************************************************/
const numArray: number[] = [0, 1, 2];

const strArr: string[] = ["Evan", "Sabrina"];

const genericNumArr: Array<number> = [0,1];

const mixedArr: (string|number|boolean)[] = [1, "Adam", 2, "Dan"];
mixedArr.push(7);
mixedArr.push("dksughak");
mixedArr.push(true);

const mixedArr2: Array<string|number|boolean> = [1, "Adam", 2, "Dan"];

/***********************************************************
 * Tuples
 ***********************************************************/
let mixTup: [string, number];
 mixTup = ["Jim", 35];

 mixTup[0].toUpperCase(); //String 
 mixTup[1].toFixed(); //number

 /***********************************************************
 * Enums
 ***********************************************************/
enum CardType {Hearts, Diamonds, Spades, Clubs}

let myCard: CardType = CardType.Hearts;
let cardName: string = CardType[2]; //Spades

 /***********************************************************
 * any Type
 * Should only use when absolutely nessisary
 * See: Interfaces
 ***********************************************************/
const data: any = 4;
const mix: any[] = [1, "Phill", false];

 /***********************************************************
 * never Type
 * values that NEVER occure
 ***********************************************************/
function error(): never {
    throw new Error('error');
}

function fail() {
    return error(); //has never type forever
}

function infinite(): never {
    while (true) { } //will break application
}

 /***********************************************************
 * null & undefined
 ***********************************************************/
let test: null = null;
let test2: undefined = undefined;
let test3: number = 1;
// test3 = undefined;

 /***********************************************************
 * void
 * No retrun allowed
 ***********************************************************/
function greet1(name: string): void {
    console.log(`Hello ${name}!`);
}

 /***********************************************************
 * functions
 * can have types as their own
 ***********************************************************/
function greet2(name: string): string{
    return `Hello ${name}!`;
}

function greet3(name: string, age: number): string{
    return `Hello ${name}, you are ${age} years old`;
}

 /***********************************************************
 * type
 * type aliasing
 * does NOT create a new type.
 * Creates a new name to refer to that type
 ***********************************************************/
type User = {
    userName: string;
    userAge: number;
};

const myUser: User = {
    userName: "Pat",
    userAge: 29
};

 /***********************************************************
 * Type Assertion
 * Useful when you are certain of a values types, and you know it may change
 ***********************************************************/
const myUser2 = {};
const myUser3 = {};
(myUser2 as User).userAge = 35;
(<User>myUser3).userAge = 25;

 /***********************************************************
 * Objects
 ***********************************************************/
const users4: {name: string, age: number}[] = [
    {
        name: "Jimbo",
        age: 40
    },
    {
        name: "David",
        age: 45
    },
    {
        name: "Karl",
        age: 27
    }
];