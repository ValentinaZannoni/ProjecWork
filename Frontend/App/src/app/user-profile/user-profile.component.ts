import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {User} from '../models/user'
import { AuthService } from '../layouts/admin-layout/auth.service';
import { ToastrService } from 'ngx-toastr';
import { ActivatedRoute } from '@angular/router';
import { Course } from '../models';
import { CommonModule, } from '@angular/common';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  constructor(private route: ActivatedRoute, private http: HttpClient, public auth : AuthService, private toastr: ToastrService) { }

  user: User = {
    id: 72387,
    name: "Valentina",
    surname: "Zannoni",
    phoneNumber: "3394873635",
    age: "10",
    role: "S",     // T = teacher , S = Student
    cf: "ZNNVNT01T52E730L",
    emailAddress: "subit@io.it",
    password: null
  }

  coursesTeacher: Course[] = [{
    id: 6487,
    title : "Prova",
    subject : "Programmazione",
    price: null,
    description : "Questo è un bel corso",
    teacher : null,
    students: null,
  },
  {
    id: 5544,
    title : "Prova2",
    subject : "Matematica",
    price: null,
    description : "Questo è un brutto corso",
    teacher : null,
    students: null,
  }
];

isTeacher:string;
tableCoursesVisible: boolean = false;
idUser: string;
  ngOnInit() {
    this.route.params.subscribe((params) => this.isTeacher = params.isTeacher);
    this.route.params.subscribe((params) => this.idUser = params.idUser);
    this.getUser();
    console.log("auth email", this.auth.email)
    
  }

  getUser(){
    this.http.get('http://192.168.33.171:80/users/' + this.auth.email).subscribe((data: any) => {
      this.user = data.map(t => Object.assign(new User(), t));
    });  
  }

  logout(){
    this.auth.isLogged = false;
  }

  updateData(){
    this.http.put("", this.user).subscribe(data => {
      console.log(data);
      this.toastr.info('<span class="now-ui-icons ui-1_bell-53"></span> Salvataggio effettuato con successo', '', {
        timeOut: 8000,
        closeButton: true,
        enableHtml: true,
        toastClass: "alert alert-success alert-with-icon",
        positionClass: 'toast-' + 'top' + '-' +  'center'
      });
    });
   
    return true;
  }


}
