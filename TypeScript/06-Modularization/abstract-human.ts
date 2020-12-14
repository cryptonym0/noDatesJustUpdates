import IPerson from "./iperson";

export default abstract class Human implements IPerson{
    name: string;
    age: number;
    constrctor(name: string){
        this.name = name;
    }
    abstract showAge(): number;
}