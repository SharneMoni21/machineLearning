import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

//import { FormGroup } from '@angular/forms';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit{

  title = 'Front-End';

  //form:FormGroup;
  shortLink: string = "";
  loading: boolean = false;
  file: File; // Variable to store file


  constructor(private auth: SharedService) { }

  ngOnInit(): void {
    // this.form = this.fb.group({
    //   title: [''],
    //   body: [''],

    // })
  }

  onChange(event)
  {
    console.log("Hello World");
    this.file = event.target.files[0];
  }

  
  submit()
  {
    this.loading = !this.loading;
    console.log(this.file);
    this.auth.send_post_request(this.file).subscribe(
      (event: any) => {
        if (typeof (event) === 'object') {
          
          // Short link via api response
          this.shortLink = event.link;
          this.loading = false; // Flag variable
        }
      }
    )
    
    // console.log("Submitted");
    // console.log(this.form.value);
    // this.auth.send_post_request(this.form.value).subscribe()

  }


}

  
  

