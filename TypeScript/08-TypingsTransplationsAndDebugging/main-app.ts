import Hero from "./hero";

const spiderman = new Hero("Spiderman");
spiderman.age = 21;
spiderman.addPower("Spin Web");
spiderman.addPower("Spider Senses");
console.log(spiderman.listPowers());
