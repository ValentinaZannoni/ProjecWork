import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Course } from '../models/course';
import { AuthService } from '../layouts/admin-layout/auth.service';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  orderby: string;
//   courses: Course[] = [{
//     id: 6487,
//     title : "Prova",
//     subject : "Programmazione",
//     price: null,
//     description : "Questo è un bel corso",
//     teacher : {
//       id: 72387,
//       name: "Valentina",
//       surname: "Zannoni",
//       phoneNumber: "3394873635",
//       age: "10",
//       role: "S",     // T = teacher , S = Student
//       cf: "ZNNVNT01T52E730L",
//       emailAddress: "subit@io.it",
//       password: null
//     },
//     students: null,
//   },
//   {
//     id: 5544,
//     title : "Prova2",
//     subject : "Matematica",
//     price: null,
//     description : "Questo è un brutto corso",
//     teacher : {
//       id:345,
//       name: "Maria",
//       surname: "Gianca",
//       phoneNumber: "6453738635",
//       age: "40",
//       role: null,   // T = teacher , S = Student
//       cf: "DRTVTH65T56N764G",
//       emailAddress: "emailprof@gmail.com",
//       password: null
//     },
//     students: null,
//   }
// ];
  courses: Course[]

  constructor(public auth: AuthService, private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
  this.getCourses()
   if(this.auth.isLogged) console.log("sono loggato")
  }

  getCourses(){
    this.http.get('http://192.168.0.80:80/courses').subscribe((data: any[]) => {
      this.courses = data.map(user => Object.assign(new Course(), user));

      console.log("aaaa", this.courses);
    });
  }
}
