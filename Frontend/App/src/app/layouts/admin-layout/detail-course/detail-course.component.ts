import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Course } from './models';

@Component({
  selector: 'detail-course',
  templateUrl: './detail-course.component.html',
  styleUrls: ['./detail-course.component.css']
})
export class DetailCourseComponent implements OnInit {

  courseid: string;

  course: Course = {
    id: 6487,
    title : "Prova",
    subject : "Programmazione",
    price: 50.00,
    description : "Questo è un bel corso",
    teacher : null,
    students: null,
  }

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe((params) => this.courseid = params.courseid);
    console.log(this.courseid)
  }

}
