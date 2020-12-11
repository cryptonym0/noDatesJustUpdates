const fname = 'Jeff';
const age = 30;

const person = {
    fname,
    age
};

console.log(person.fname);
console.log(fname);

// [LOG]: "Jeff"
// [LOG]: "Jeff"

/***********************************************************
 * Template Literals
 * It's just a syntax
 ***********************************************************/
const name1 = 'Steve';
console.log(`Hello ${name1}`);

//how about an API key
import http = require('http');
const apiKey = 'abc';
http.get(`https://my.api/data?api=${apiKey}`);