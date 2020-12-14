/***********************************************************
 * Abstract Classes
 * Hide complexity
 ***********************************************************/
abstract class HumanAC {
    public name: string;
    public age: number;
    constructor(name: string){
        this.name = name;
    }

    abstract greet(): void;
}


class PersonE extends HumanAC{
    constructor(name: string){
        super(name);
    }
    greet(): void {
        console.log(`Hello Friend.`);
    }
}

let john = new PersonE("John");
john.greet();