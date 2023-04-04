import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Course } from '../models/course';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  orderby: string;
  courses: Course[] = [{
    id: 6487,
    title : "Prova",
    subject : "Programmazione",
    price: null,
    description : "Questo è un bel corso",
  },
  {
    id: 5544,
    title : "Prova2",
    subject : "Matematica",
    price: null,
    description : "Questo è un brutto corso",

  }
];

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
   this.getCourses()
  }

  getCourses(){
    // this.http.get('http://192.168.33.171:80/courses').subscribe((data: any[]) => {
    //   const users = data.map(user => Object.assign(new Course(), user));

    //   console.log(users);
    // });
  }
}
