System.register("iperson", [], function (exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    return {
        setters: [],
        execute: function () {
        }
    };
});
System.register("abstract-human", [], function (exports_2, context_2) {
    "use strict";
    var Human;
    var __moduleName = context_2 && context_2.id;
    return {
        setters: [],
        execute: function () {
            Human = class Human {
                constrctor(name) {
                    this.name = name;
                }
            };
            exports_2("default", Human);
        }
    };
});
System.register("person", ["abstract-human"], function (exports_3, context_3) {
    "use strict";
    var abstract_human_1, Person;
    var __moduleName = context_3 && context_3.id;
    return {
        setters: [
            function (abstract_human_1_1) {
                abstract_human_1 = abstract_human_1_1;
            }
        ],
        execute: function () {
            Person = class Person extends abstract_human_1.default {
                constructor(name) {
                    super();
                }
                showAge() {
                    return this.age;
                }
            };
            exports_3("default", Person);
        }
    };
});
System.register("ihero", [], function (exports_4, context_4) {
    "use strict";
    var __moduleName = context_4 && context_4.id;
    return {
        setters: [],
        execute: function () {
        }
    };
});
System.register("hero", ["person"], function (exports_5, context_5) {
    "use strict";
    var person_1, Hero;
    var __moduleName = context_5 && context_5.id;
    return {
        setters: [
            function (person_1_1) {
                person_1 = person_1_1;
            }
        ],
        execute: function () {
            Hero = class Hero extends person_1.default {
                constructor(name) {
                    super(name);
                    this.superpowers = [];
                }
                addPower(power) {
                    this.superpowers.push(power);
                }
                listPowers() {
                    return this.superpowers;
                }
            };
            exports_5("default", Hero);
        }
    };
});
System.register("main-app", ["hero"], function (exports_6, context_6) {
    "use strict";
    var hero_1, spiderman;
    var __moduleName = context_6 && context_6.id;
    return {
        setters: [
            function (hero_1_1) {
                hero_1 = hero_1_1;
            }
        ],
        execute: function () {
            spiderman = new hero_1.default("Spiderman");
            spiderman.age = 21;
            spiderman.addPower("Spin Web");
            spiderman.addPower("Spider Senses");
            console.log(spiderman.listPowers());
        }
    };
});
// npm i --save @types/underscore
// npm i --save underscore
// npm i --save @types/node  
System.register("third-party-libs", ["underscore", "fs"], function (exports_7, context_7) {
    "use strict";
    var _, fs, users, maxAge, file;
    var __moduleName = context_7 && context_7.id;
    return {
        setters: [
            function (_1) {
                _ = _1;
            },
            function (fs_1) {
                fs = fs_1;
            }
        ],
        execute: function () {// npm i --save @types/underscore
            // npm i --save underscore
            // npm i --save @types/node  
            users = [{
                    name: "Evan",
                    age: 23
                }, {
                    name: "Marco",
                    age: 30
                }, {
                    name: "Kris",
                    age: 23
                }];
            maxAge = _.max(users, user => user.age);
            console.log(maxAge);
            file = fs.readFileSync('./test.ts', 'utf-8');
        }
    };
});
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYnVuZGxlLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vaXBlcnNvbi50cyIsIi4uL2Fic3RyYWN0LWh1bWFuLnRzIiwiLi4vcGVyc29uLnRzIiwiLi4vaWhlcm8udHMiLCIuLi9oZXJvLnRzIiwiLi4vbWFpbi1hcHAudHMiLCIuLi90aGlyZC1wYXJ0eS1saWJzLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7OztRQUdDLENBQUM7Ozs7Ozs7Ozs7WUNERixRQUFBLE1BQThCLEtBQUs7Z0JBRy9CLFVBQVUsQ0FBQyxJQUFZO29CQUNuQixJQUFJLENBQUMsSUFBSSxHQUFHLElBQUksQ0FBQztnQkFDckIsQ0FBQzthQUVKLENBQUE7O1FBQUEsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7WUNQRixTQUFBLE1BQXFCLE1BQU8sU0FBUSx3QkFBSztnQkFDckMsWUFBWSxJQUFZO29CQUNwQixLQUFLLEVBQUUsQ0FBQztnQkFDWixDQUFDO2dCQUNELE9BQU87b0JBQ0gsT0FBTyxJQUFJLENBQUMsR0FBRyxDQUFDO2dCQUNwQixDQUFDO2FBQ0osQ0FBQTs7UUFFRCxDQUFDOzs7Ozs7Ozs7UUNQQSxDQUFDOzs7Ozs7Ozs7Ozs7OztZQ0RGLE9BQUEsTUFBcUIsSUFBSyxTQUFRLGdCQUFNO2dCQUVwQyxZQUFZLElBQVk7b0JBQ3BCLEtBQUssQ0FBQyxJQUFJLENBQUMsQ0FBQztvQkFGaEIsZ0JBQVcsR0FBYSxFQUFFLENBQUM7Z0JBRzNCLENBQUM7Z0JBQ0QsUUFBUSxDQUFDLEtBQWE7b0JBQ2xCLElBQUksQ0FBQyxXQUFXLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxDQUFDO2dCQUNqQyxDQUFDO2dCQUNELFVBQVU7b0JBQ04sT0FBTyxJQUFJLENBQUMsV0FBVyxDQUFDO2dCQUM1QixDQUFDO2FBQ0osQ0FBQTs7UUFBQSxDQUFDOzs7Ozs7Ozs7Ozs7OztZQ1pJLFNBQVMsR0FBRyxJQUFJLGNBQUksQ0FBQyxXQUFXLENBQUMsQ0FBQztZQUN4QyxTQUFTLENBQUMsR0FBRyxHQUFHLEVBQUUsQ0FBQztZQUNuQixTQUFTLENBQUMsUUFBUSxDQUFDLFVBQVUsQ0FBQyxDQUFDO1lBQy9CLFNBQVMsQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLENBQUM7WUFDcEMsT0FBTyxDQUFDLEdBQUcsQ0FBQyxTQUFTLENBQUMsVUFBVSxFQUFFLENBQUMsQ0FBQztRQUNwQyxDQUFDOzs7QUNQRCxpQ0FBaUM7QUFDakMsMEJBQTBCO0FBQzFCLDZCQUE2Qjs7Ozs7Ozs7Ozs7Ozs7OEJBRjdCLGlDQUFpQztZQUNqQywwQkFBMEI7WUFDMUIsNkJBQTZCO1lBS3ZCLEtBQUssR0FBb0MsQ0FBQztvQkFDNUMsSUFBSSxFQUFFLE1BQU07b0JBQ1osR0FBRyxFQUFFLEVBQUU7aUJBQ1YsRUFBRTtvQkFDQyxJQUFJLEVBQUUsT0FBTztvQkFDYixHQUFHLEVBQUMsRUFBRTtpQkFDVCxFQUFFO29CQUNDLElBQUksRUFBRSxNQUFNO29CQUNaLEdBQUcsRUFBRSxFQUFFO2lCQUNWLENBQUMsQ0FBQztZQUVHLE1BQU0sR0FBRyxDQUFDLENBQUMsR0FBRyxDQUFDLEtBQUssRUFBRSxJQUFJLENBQUMsRUFBRSxDQUFDLElBQUksQ0FBQyxHQUFHLENBQUMsQ0FBQztZQUM5QyxPQUFPLENBQUMsR0FBRyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1lBR2QsSUFBSSxHQUFXLEVBQUUsQ0FBQyxZQUFZLENBQUMsV0FBVyxFQUFFLE9BQU8sQ0FBQyxDQUFDO1FBQUEsQ0FBQyIsInNvdXJjZXNDb250ZW50IjpbImV4cG9ydCBkZWZhdWx0IGludGVyZmFjZSBJUGVyc29ue1xuICAgIG5hbWU6IHN0cmluZztcbiAgICBhZ2U6IE51bWJlcjtcbn0iLCJpbXBvcnQgSVBlcnNvbiBmcm9tIFwiLi9pcGVyc29uXCI7XG5cbmV4cG9ydCBkZWZhdWx0IGFic3RyYWN0IGNsYXNzIEh1bWFuIGltcGxlbWVudHMgSVBlcnNvbntcbiAgICBuYW1lOiBzdHJpbmc7XG4gICAgYWdlOiBudW1iZXI7XG4gICAgY29uc3RyY3RvcihuYW1lOiBzdHJpbmcpe1xuICAgICAgICB0aGlzLm5hbWUgPSBuYW1lO1xuICAgIH1cbiAgICBhYnN0cmFjdCBzaG93QWdlKCk6IG51bWJlcjtcbn0iLCJpbXBvcnQgSHVtYW4gZnJvbSBcIi4vYWJzdHJhY3QtaHVtYW5cIjtcblxuZXhwb3J0IGRlZmF1bHQgY2xhc3MgUGVyc29uIGV4dGVuZHMgSHVtYW4ge1xuICAgIGNvbnN0cnVjdG9yKG5hbWU6IHN0cmluZyl7XG4gICAgICAgIHN1cGVyKCk7XG4gICAgfVxuICAgIHNob3dBZ2UoKTogbnVtYmVye1xuICAgICAgICByZXR1cm4gdGhpcy5hZ2U7XG4gICAgfVxufVxuXG4iLCJpbXBvcnQgSVBlcnNvbiBmcm9tIFwiLi9pcGVyc29uXCI7XG5cbmV4cG9ydCBkZWZhdWx0IGludGVyZmFjZSBJSGVybyBleHRlbmRzIElQZXJzb24ge1xuICAgIHN1cGVycG93ZXJzOiBzdHJpbmdbXTtcbn0iLCJpbXBvcnQgUGVyc29uIGZyb20gXCIuL3BlcnNvblwiO1xuaW1wb3J0IElIZXJvIGZyb20gXCIuL2loZXJvXCI7XG5cbmV4cG9ydCBkZWZhdWx0IGNsYXNzIEhlcm8gZXh0ZW5kcyBQZXJzb24gaW1wbGVtZW50cyBJSGVyb3tcbiAgICBzdXBlcnBvd2Vyczogc3RyaW5nW10gPSBbXTtcbiAgICBjb25zdHJ1Y3RvcihuYW1lOiBzdHJpbmcpe1xuICAgICAgICBzdXBlcihuYW1lKTtcbiAgICB9XG4gICAgYWRkUG93ZXIocG93ZXI6IHN0cmluZyk6IHZvaWR7XG4gICAgICAgIHRoaXMuc3VwZXJwb3dlcnMucHVzaChwb3dlcik7XG4gICAgfVxuICAgIGxpc3RQb3dlcnMoKTogc3RyaW5nW117XG4gICAgICAgIHJldHVybiB0aGlzLnN1cGVycG93ZXJzO1xuICAgIH1cbn0iLCJpbXBvcnQgSGVybyBmcm9tIFwiLi9oZXJvXCI7XG5cbmNvbnN0IHNwaWRlcm1hbiA9IG5ldyBIZXJvKFwiU3BpZGVybWFuXCIpO1xuc3BpZGVybWFuLmFnZSA9IDIxO1xuc3BpZGVybWFuLmFkZFBvd2VyKFwiU3BpbiBXZWJcIik7XG5zcGlkZXJtYW4uYWRkUG93ZXIoXCJTcGlkZXIgU2Vuc2VzXCIpO1xuY29uc29sZS5sb2coc3BpZGVybWFuLmxpc3RQb3dlcnMoKSk7XG4iLCIvLyBucG0gaSAtLXNhdmUgQHR5cGVzL3VuZGVyc2NvcmVcbi8vIG5wbSBpIC0tc2F2ZSB1bmRlcnNjb3JlXG4vLyBucG0gaSAtLXNhdmUgQHR5cGVzL25vZGUgIFxuXG5pbXBvcnQgKiBhcyBfIGZyb20gXCJ1bmRlcnNjb3JlXCI7XG5pbXBvcnQgKiBhcyBmcyBmcm9tIFwiZnNcIjtcblxuY29uc3QgdXNlcnM6IHsgbmFtZTogc3RyaW5nLCBhZ2U6IG51bWJlciB9W10gPSBbe1xuICAgIG5hbWU6IFwiRXZhblwiLFxuICAgIGFnZTogMjNcbn0sIHtcbiAgICBuYW1lOiBcIk1hcmNvXCIsXG4gICAgYWdlOjMwXG59LCB7XG4gICAgbmFtZTogXCJLcmlzXCIsXG4gICAgYWdlOiAyM1xufV07XG5cbmNvbnN0IG1heEFnZSA9IF8ubWF4KHVzZXJzLCB1c2VyID0+IHVzZXIuYWdlKTtcbmNvbnNvbGUubG9nKG1heEFnZSk7XG5cblxuY29uc3QgZmlsZTogc3RyaW5nID0gZnMucmVhZEZpbGVTeW5jKCcuL3Rlc3QudHMnLCAndXRmLTgnKTsiXX0=