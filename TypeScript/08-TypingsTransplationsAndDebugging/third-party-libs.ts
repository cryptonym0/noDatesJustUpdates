// npm i --save @types/underscore
// npm i --save underscore
// npm i --save @types/node  

import * as _ from "underscore";
import * as fs from "fs";

const users: { name: string, age: number }[] = [{
    name: "Evan",
    age: 23
}, {
    name: "Marco",
    age:30
}, {
    name: "Kris",
    age: 23
}];

const maxAge = _.max(users, user => user.age);
console.log(maxAge);


const file: string = fs.readFileSync('./test.ts', 'utf-8');