export class User {
    // constructor(jsonStr: string) {
    //     let jsonObj = JSON.parse(jsonStr);
    //     for (let prop in jsonObj) {
    //         this[prop] = jsonObj[prop];
    //     }
    // }
    constructor(){

    }
    id: number;
    name: string;
    surname: string;
    phoneNumber: string;
    age: string;
    role: string;     // T = teacher , S = Student
    cf: string;
    emailAddress: string;
    password: string;
}