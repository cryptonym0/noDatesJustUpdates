import { pi } from "./utils";
console.log(pi);

import { pi as math} from "./utils";
console.log(math);

import * as someMath from "./utils";
console.log(someMath.pi);

import MathModule from "./utils";
const myMath = new MathModule();
console.log(myMath.add(5,6));

import { MathModule2 } from "./utils";
const myMath2 = new MathModule2();
console.log(myMath2.add(5,6));