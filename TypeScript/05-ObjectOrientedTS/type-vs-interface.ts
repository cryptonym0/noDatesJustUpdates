type User = {
    name: string;
    age: number;
};

 interface User2 {
    name: string;
    age: number;
 };

 interface User2{
     address: string;
 };

 //Typescript will MERGE the 2 interfaces together.
 //Interface can use the extends and implements keywords.

 let userX: User = {
     name: "Brad",
     age: 1
 }

