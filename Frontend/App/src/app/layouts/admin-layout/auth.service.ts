import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class AuthService {

  constructor() { }

  public name: string;
  public surname: string;
  public phoneNumber: string;
  public role: string;
  public cf: string;
  public email: string;
  public password: string;
  public isLogged: boolean = false; 
}