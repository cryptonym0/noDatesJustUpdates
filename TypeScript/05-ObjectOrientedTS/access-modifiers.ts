/***********************************************************
 * Access Modifiers: Public, Private, Protected, and Read-Only
 * If you do nut specify then public is assumed
***********************************************************/

/***********************************************************
 * Public
 * In TypeScript, each member is public by default. 
 * You may still mark a member public explicitly. 
***********************************************************/
class EmployeePublic {
    public id: number;
    public firstName: string;
    public lastName: string;

    constructor(id: number, firstName: string, lastName: string) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public getFullName() {
        return this.firstName + ' ' + this.lastName;
    }
}

console.log("Public Logs:\n");
// create Employee class object
let employee1 = new EmployeePublic(100, 'Ramesh', 'Fadatare');
console.log(employee1);
console.log(employee1.getFullName());

/***********************************************************
* Private
* When a member is marked private, it cannot be accessed from 
* outside of its containing class.
***********************************************************/
class EmployeePrivate {
    private id: number;
    public firstName: string;
    public lastName: string;

    public getFullName() {
        return this.firstName + ' ' + this.lastName;
    }
}

console.log("\nPrivate Logs:\n");
// create Employee class object
let employee2 = new EmployeePrivate();
// employee2.id = 100; // ERROR Property 'id' is private and only accessible within class 'Employee'.ts
employee2.firstName = 'Herald';

console.log(employee2);
console.log(employee2.getFullName());

  /***********************************************************
 * Protected
 * The protected modifier acts much like the private modifier 
 * with the exception that members declared protected can also 
 * be accessed within deriving classes.
 * 
 * A constructor may also be marked protected. 
 * This means that the class cannot be instantiated outside 
 * of its containing class, but can be extended. 
 ***********************************************************/
class PersonProtected {
    protected name: string;
    //Protected constructor
    protected constructor(name: string) {
        this.name = name;
    }
}

class EmployeeProtected extends PersonProtected {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    public getElevatorPitch() {
        return `Hello, my name is ${this.name} and I work in ${this.department}.`;
    }
}

console.log("\nProtected Logs:\n");
let howard = new EmployeeProtected("Howard", "Sales");
console.log(howard.getElevatorPitch());
// let john = new Person("John"); // Error: The 'Person' constructor is protected
// console.log(howard.name); // ERROR: Property 'name' is protected and only accessible within class 'Person' and its subclasses.

  /***********************************************************
 * Read Only
 * You can make properties readonly by using the readonly keyword. 
 * Readonly properties must be initialized at their declaration or in the constructor. 
 ***********************************************************/
class EmployeeReadOnly{
    readonly id: number;
    public firstName: string;
    readonly lastName: string;

    constructor(id: number, firstName: string, lastName: string){
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public getFullName(){
        return this.firstName + ' ' + this.lastName;
    }
}

console.log("\nRead Only Logs:\n");
// create Employee class object
let employee = new EmployeeReadOnly(100, 'Ramesh', 'Fadatare');
// employee.id = 200; // Error: Cannot assign to 'id' because it is a read-only property.
// employee.lastName = 'Kapoor'; // Error: Cannot assign to 'lastName' because it is a read-only property
console.log(employee);
console.log(employee.getFullName());