import { User } from "./user";

export class Course {
    constructor(){
        this.students = [];
    }
    id: number;
    title: string;
    subject: string;
    description: string;
    price: number;
    students: User[];
    teacher?: User;
}