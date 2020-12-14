 /***********************************************************
 * interfaces
 * provide a powerful way to define an entity that must conform by definition
 ***********************************************************/

 interface IUser {
     name: string;
     readonly age: number;
     address?: string; //optional
 }

 //  myUser.age = 30; //not allowed because read only!

 interface IGreet {
     (name: string, language: string): string
 }

 let hello: IGreet;
 hello = function(n: string, lang: string){
     if(lang === "en"){
        return `Hello ${n}`;
     } else if(lang === "fr"){
        return `Bonjour ${n}`;
     }else{
        return `Hola ${n}`;
     }
 }

 hello("Terry", "en");
 console.log( hello("Terry", "en"));
 console.log( hello("Terry", "fr"));
 console.log( hello("Terry", ""));
 let myUser: IUser = {
     name: "John",
     age: 55,
 }

/***********************************************************
 * Interfaces: Extends
 ***********************************************************/
interface IPerson {
    name: string;
}

interface IHero extends IPerson{
    superPower: string;
}

let regularJoe: IPerson = {
    name: "Joe"
}

let batman: IHero = {
    name: "bruce",
    superPower: "money"
}

  /***********************************************************
 * Interfaces: Eindex Signature
 ***********************************************************/
interface IPet {
    name: string;
    readonly age: number;
    address?: string;
    [property: string]: any;
}

let princess: IPet = {
    name: "princess",
    age: 2,
    xyz: "asdf",
    test: 1,
    huhok: 'ok',
    true: true
}

princess.test; //access the 1