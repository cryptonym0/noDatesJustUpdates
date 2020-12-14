interface IPerson{
    name: string;
    age: Number;
}

interface IHero extends IPerson {
    superpowers: string[];
}

abstract class Human implements IPerson{
    name: string;
    age: number;
    constrctor(name: string){
        this.name = name;
    }
    abstract showAge(): number;
}

class Person extends Human {
    constructor(name: string){
        super();
    }
    showAge(): number{
        return this.age;
    }
}

class Hero extends Person implements IHero{
    superpowers: string[] = [];
    constructor(name: string){
        super(name);
    }
    addPower(power: string): void{
        this.superpowers.push(power);
    }
    listPowers(): string[]{
        return this.superpowers;
    }
}

let spiderman = new Hero("Spiderman");
spiderman.age = 21;
spiderman.addPower("Spin Web");
spiderman.addPower("Spider Senses");
console.log(spiderman.listPowers());
