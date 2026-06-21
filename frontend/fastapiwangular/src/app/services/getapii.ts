import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Getapii {
     private API_host = "http://127.0.0.1:8000";
constructor(private http:HttpClient){}
     getapi(): Observable<any>{
      console.log("service");
      return this.http.get(`${this.API_host}/dis`)
     }
      
     }

