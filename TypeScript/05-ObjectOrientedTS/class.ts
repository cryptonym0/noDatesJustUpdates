class Person{
    name: string
    constructor(name: string){
        this.name = name;
    }
    greet(): string {
        return `Hello ${this.name}`;
    }
}


class Hero extends Person {
    superPowers: string[] = [];
    constructor(name: string){
        super(name);
    }
    addPower(power: string): void {
        this.superPowers.push(power);
    }
    listPowers(): string[] {
        return this.superPowers;
    }
}

let myHero = new Hero("Bruce");
myHero.addPower("money");
console.log(myHero.listPowers());
myHero.addPower("guns");
console.log(myHero.listPowers());
// [ 'money' ]
// [ 'money', 'guns' ]