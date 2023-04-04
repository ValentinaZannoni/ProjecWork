import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {User} from '../models/user'

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  getData(){
    this.http
       .get<any>('http://192.168.33.171:80/items')
      .subscribe(data => {
        const user = Object.assign(new User(), data);
      });

      }


}
