import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {User} from '../models/user'
import { AuthService } from '../layouts/admin-layout/auth.service';
import { ToastrService } from 'ngx-toastr';
import { ActivatedRoute } from '@angular/router';
import { Course } from '../models';
import { CommonModule, } from '@angular/common';
import { Res } from '../models/res';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  constructor(private route: ActivatedRoute, private http: HttpClient, public auth : AuthService, private toastr: ToastrService) { }

  user:User;
  coursesTeacher: Course[];
  // user: User = {
  //   id: 72387,
  //   name: "Valentina",
  //   surname: "Zannoni",
  //   phoneNumber: "3394873635",
  //   age: "10",
  //   role: "S",     // T = teacher , S = Student
  //   cf: "ZNNVNT01T52E730L",
  //   emailAddress: "subit@io.it",
  //   password: null
  // }


//   coursesTeacher: Course[] = [{
//     id: 6487,
//     title : "Prova",
//     subject : "Programmazione",
//     price: null,
//     description : "Questo è un bel corso",
//     teacherId : 0,
//     students: null,
//   },
//   {
//     id: 5544,
//     title : "Prova2",
//     subject : "Matematica",
//     price: null,
//     description : "Questo è un brutto corso",
//     teacherId : 0,
//     students: null,
//   }
// ];

isTeacher:string;
tableCoursesVisible: boolean = false;
idTeacher: string;
  ngOnInit() {
    this.route.params.subscribe((params) => this.isTeacher = params.isTeacher);
    this.route.params.subscribe((params) => this.idTeacher = params.idUser);
    if(this.isTeacher == "S") this.getUser()
    if(this.isTeacher == "T") {
      this.getTeacher()
      this.getTeacherCourses()
    }
  }

   getUser(){
     this.http.get('http://192.168.0.14:80/users/mail/' + this.auth.email).subscribe((data: any) => {
       this.user = Object.assign(new User(), data);
     });  
   }

  getTeacher(){
    this.http.get('http://192.168.0.14:80/users/' + this.idTeacher).subscribe((data: any) => {
      this.user = Object.assign(new User(), data);
    });  
  }

  getTeacherCourses(){
    this.http.get('http://192.168.0.14:80/courses/teacher/' + this.idTeacher).subscribe((data: any[]) => {
      this.coursesTeacher = data.map(courses => Object.assign(new Course(), courses));
    });
  }

  logout(){
    this.auth.isLogged = false;
  }

  updateData(){
    this.http.put("http://192.168.0.14:80/users/" + this.user.id, this.user).subscribe(data => {
      this.res = Object.assign(new Res(), data);
      if(this.res.response == "user modified"){
        this.toastr.info('<span class="now-ui-icons ui-1_bell-53"></span> Salvataggio effettuato con successo', '', {
          timeOut: 8000,
          closeButton: true,
          enableHtml: true,
          toastClass: "alert alert-success alert-with-icon",
          positionClass: 'toast-' + 'top' + '-' +  'center'
        });
      } else {
        this.toastr.info('<span class="now-ui-icons ui-1_bell-53"></span> Errori nella modifica', '', {
          timeOut: 8000,
          closeButton: true,
          enableHtml: true,
          toastClass: "alert alert-danger alert-with-icon",
          positionClass: 'toast-' + 'top' + '-' +  'center'
        });
      }
    });
    
    return true;
    
  }

  res : Res;

  deleteAccount(){
    this.http.delete('http://192.168.0.14:80/users/delete/'+ this.auth.email).subscribe(data => {
      this.res = Object.assign(new Res(), data);
      console.log(this.res.response);
      if(this.res.response == "User deleted"){
        this.auth.isLogged = false;
      this.toastr.info('<span class="now-ui-icons ui-1_bell-53"></span> Account eliminato con successo', '', {
        timeOut: 8000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-danger alert-with-icon",
        positionClass: 'toast-' + 'top' + '-' +  'center'
      });
      }
    });
  }

}
