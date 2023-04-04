import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  orderby: string;

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
   console.log("aaaaaaaaaaaaaaaaa")
   this.getProva()
  }

  getProva(){
    // questo è per i parametri 
    // let headers = new HttpHeaders({
    //   'x-rapidapi-host': 'random-facts2.p.rapidapi.com',
    //   'x-rapidapi-key': 'your-api-key'
    // });
    this.http
    // con parametri 

      // .get<any>('https://random-facts2.p.rapidapi.com/getfact', {
      //   headers: headers
      // })

     // senza parametri 

       .get<any>('http://192.168.33.171:80/items')
      .subscribe(data => {
        console.log(data);
      });
      // console.log("data");

      }

  
  getProvaWithFilters(){
  //   this.route.queryParamMap
  //   .subscribe((params) => {
  //     this.paramsObject = { ...params.keys, ...params };
  //     console.log(this.paramsObject);
  //   }
  // );
  
  }

}