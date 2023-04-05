import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class AuthService {

  constructor() { }

  public isLogged: boolean = false;
  public email: string;
  public password: string;
}