const isAdmin: boolean = true;
const myNumber: number = 100;
const user: string = "Marco";
let welcome: string;

if (isAdmin) {
welcome = `Hello ${user}`;
} else{
    welcome = `${user} is not an Admin,`; 
}

console.log(welcome);
console.log(welcome, "hihihi");