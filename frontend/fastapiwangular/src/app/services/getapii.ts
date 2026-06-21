import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Getapii {
     private API_host = "https://fastapi-backend.icyocean-28693c97.westus2.azurecontainerapps.io/";
constructor(private http:HttpClient){}
     getapi(): Observable<any>{
      console.log("service");
      return this.http.get(`${this.API_host}/dis`)
     }
      
     }

