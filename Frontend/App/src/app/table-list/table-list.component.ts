import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  orderby: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
   this.getProva()
  }

  getProva(){
  //   this.route.queryParams
  //   .subscribe(params => {
  //     console.log(params); // { orderby: "price" }
  //     this.orderby = params.orderby;
  //     console.log(this.orderby); // price
  //   }
  // );
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
