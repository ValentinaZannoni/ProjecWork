import { Injectable } from '@angular/core';
import { User } from './models';

@Injectable({
  providedIn: 'root',
})

export class AuthService {

  constructor() { }

  public name: string;
  public age: number;
  public surname: string;
  public phoneNumber: number;
  public role: string;
  public cf: string;
  public email: string;
  public password: string;
  public id: number;
  public isLogged: boolean = false; 

  public coursesSubscribed: User[];
  public coursesUnubscribed: User[];

}