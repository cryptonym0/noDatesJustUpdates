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
interface IPerson1 {
    name: string;
}

interface IHero1 extends IPerson1{
    superPower: string;
}

let regularJoe: IPerson1 = {
    name: "Joe"
}

let batman: IHero1 = {
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

/***********************************************************
 * Interfaces: Class Implementing an Interface
***********************************************************/
interface IPerson{
    name:string;
}
class PersonImplement{
    name: string
    constructor(name: string){
        this.name = name;
    }
    greet(): string {
        return `Hello ${this.name}`;
    }
}