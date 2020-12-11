/***********************************************************
 * Classes
 * 3 keywords
 * Class
 * extends
 * super
 ***********************************************************/

/***********************************************************
 * Class
 ***********************************************************/
class Car {
    constructor(make: String, colour: String, speed: number) {
        this.make = make;
        this.colour = colour;
        this.speed = speed;
    }

    getMaxSpeed(){
        return `Maximun speed is ${this.speed} km/h.`;
    }
}

const car = new Car('Volvo', 'Red', 250);
console.log(car.getMaxSpeed());
//[LOG]: "Maximun speed is 200 km/h."

/***********************************************************
 * extends
 ***********************************************************/
class Truck extends Car {
    getMaxSpeed(): string {
        return `Maximun Truck speed is ${this.speed} km/h.`;
    }
    getMake(): string {
        return `This Truck is a ${this.make}.`;
    }
}

const truck = new Truck('Ford', 'Yellow', 170);
console.log(truck.getMaxSpeed(), truck.getMake());
//[LOG]: "Maximun Truck speed is 170 km/h.",  "This Truck is a Ford."

/***********************************************************
 * super
 ***********************************************************/
class Person{
    name: string;

    constructor(name: String){
        this.name = name;
    }
    introduce() {
        return `Hello ${this.name}`;
    }
}

class SuperHero extends Person {
    power: string;
    constructor(name: String, power: String){
        super(name);
        this.power = power;
    }

    introduce(){
        return `${super.introduce()}. Your superpower: ${this.power}`;
    }
}

const peter = new SuperHero(`Spiderman`, `Spider Abilities`)
console.log(peter.introduce());
//[LOG]: "Hello Peter. Your superpower: Spider Abilities"