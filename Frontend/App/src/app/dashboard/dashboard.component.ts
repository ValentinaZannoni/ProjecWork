import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Course } from '../models/course';
import { AuthService } from '../layouts/admin-layout/auth.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
   courses: Course[];
  
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

  constructor( public auth : AuthService, private http: HttpClient) { }

  ngOnInit() {
    // this.getCourses();
    this.getCoursesNotFollowe();
  }

  getCourses(){
    this.http.get('http://192.168.220.1:80/courses').subscribe((data: any[]) => {
      this.courses = data.map(t => Object.assign(new Course(), t));
    });
  }

  getCoursesNotFollowe(){
    this.http.get('http://192.168.220.1:80/courses/not_subscribed/'+ this.auth.id).subscribe((data: any[]) => {
      this.auth.coursesUnubscribed = data.map(t => Object.assign(new Course(), t));
    });
  }

}
