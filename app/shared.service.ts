import { Injectable, Type } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  message: String;
  constructor(private http:HttpClient) { }
  
  server_address = "http://127.0.0.1:5000";
  

  send_post_request(file): Observable<any>{
    const formdata = new FormData();  // Create form data
    
    formdata.append("file", file, file.name);  // Store form name as "file" with file data
    return this.http.post(this.server_address, formdata);  // Make http post request over api with formData as req [JSON.stringify(data)]
  }
  
  setMessage(data)
  {
    this.message = data
  }

  getMessage()
  {
    return this.message
  }
}
