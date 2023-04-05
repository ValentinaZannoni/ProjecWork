import { Component} from '@angular/core';
import { AuthService } from './layouts/admin-layout/auth.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(public auth : AuthService) {
    // // Subscribe and listen for any changes
    // this.globalService.customVariable.subscribe({
    //   next: newValue => console.log('Update Detected:', newValue)
    // });
    // // Silently update the property on the object after 2.5s
    
  }
}
