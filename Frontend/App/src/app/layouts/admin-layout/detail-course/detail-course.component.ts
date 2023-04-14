import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Course } from '../models';

@Component({
  selector: 'detail-course',
  templateUrl: './detail-course.component.html',
  styleUrls: ['./detail-course.component.css']
})
export class DetailCourseComponent implements OnInit {

  courseid: string;

  constructor(private router: Router, private toastr: ToastrService, private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
    this.route.params.subscribe((params) => this.courseid = params.courseid);
    console.log(this.courseid)
    this.getData();
  }

   course: Course;

 

  getData(){
    this.http.get('http://192.168.220.1:80/courses/' + this.courseid).subscribe((data: any) => {
      //this.course = data.map(t => Object.assign(new Course(), t));
      this.course = Object.assign(new Course(), data);
      console.log("aaaaaa", this.course)
    });
  }

  Unsubscribe(){
    this.toastr.info('<span class="now-ui-icons ui-1_bell-53"></span> Disiscrizione avvenuta con successo', '', {
      timeOut: 8000,
      closeButton: true,
      enableHtml: true,
      toastClass: "alert alert-success alert-with-icon",
      positionClass: 'toast-' + 'top' + '-' +  'center'
    });

    this.router.navigate(['/table-list']);
  }


}
