import { Component } from '@angular/core';
import { Getapii } from '../../services/getapii';
import { JsonPipe } from '@angular/common';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-display',
  imports: [JsonPipe,CommonModule],
  templateUrl: './display.html',
  styleUrl: './display.css',
})
export class Display {
   data:any;
constructor(private apiget:Getapii){}
  getresults(){
    console.log("hey");
    this.apiget.getapi().subscribe((res)=>{
      this.data =res;
      console.log(this.data)
    });
   
// console.log('Button clicked, calling service...');
//     this.apiget.getapi().subscribe((res) => {
//       console.log('Response from backend:', res);
//       this.data = res;
//     });
  }
}
