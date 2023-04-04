import { Component, OnInit } from '@angular/core';
import * as Chartist from 'chartist';
import { Course } from '../models/course';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
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
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 2233,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 1123,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 4768,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 1232,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 4567,
    title : "Prova2",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 3456,
    title : "Prova8",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

  },
  {
    id: 8976,
    title : "Prova5",
    subject : "Matematica",
    price: 44.6,
    description : "Questo è un brutto corso",

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
  constructor() { }

  ngOnInit() {

  }
}
