import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Course } from '../models/course';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  // courses: Course[];
  courses: Course[] = [{
    id: 6487,
    title : "Prova",
    subject : "Programmazione",
    price: null,
    description : "Questo è un bel corso jshfkasfjkshedfhjsbdc djcksdkjcbsjkcd sdjkcbskdjfbcsjkcbs",
    teacher : null,
    students: null,
  },
  {
    id: 5544,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,
  },
  {
    id: 2233,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,
  },
  {
    id: 1123,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  },
  {
    id: 4768,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  },
  {
    id: 1232,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  },
  {
    id: 4567,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  },
  {
    id: 3456,
    title : "Prova8",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  },
  {
    id: 8976,
    title : "Prova5",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,

  }
];
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }

  public chartHovered(e:any):void {
    console.log(e);
  }
  public hexToRGB(hex, alpha) {
    var r = parseInt(hex.slice(1, 3), 16),
      g = parseInt(hex.slice(3, 5), 16),
      b = parseInt(hex.slice(5, 7), 16);

    if (alpha) {
      return "rgba(" + r + ", " + g + ", " + b + ", " + alpha + ")";
    } else {
      return "rgb(" + r + ", " + g + ", " + b + ")";
    }
  }

  constructor(private http: HttpClient) { }

  ngOnInit() {
    //this.getCourses();
  }

  getCourses(){
    this.http.get('http://192.168.33.171:80/courses').subscribe((data: any[]) => {
      this.courses = data.map(t => Object.assign(new Course(), t));
    });
  }

}
