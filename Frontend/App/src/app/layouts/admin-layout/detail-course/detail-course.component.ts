import { HttpClient } from '@angular/common/http';
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

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
    this.route.params.subscribe((params) => this.courseid = params.courseid);
    console.log(this.courseid)
  }

  // course: Course;

  course: Course = {
    id: 6487,
    title : "Corso di C#",
    subject : "Programmazione",
    price: 50,
    description : "Questo è un bel corso",
    teacher : {
      id:345,
      name: "Maria",
      surname: "Gianca",
      phoneNumber: "6453738635",
      age: "40",
      role: null,   // T = teacher , S = Student
      cf: "DRTVTH65T56N764G",
      emailAddress: "emailprof@gmail.com",
      password: null
    },
    students: null,
  };


  getData(){
    this.http.get('http://192.168.33.171:80/courses/' + this.courseid).subscribe((data: any) => {
      this.course = data.map(t => Object.assign(new Course(), t));
    });
  }


}
