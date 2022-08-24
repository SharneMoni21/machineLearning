import { Component, OnInit } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  title = 'Machine Learning Future Prediction';
  angForm: FormGroup;
  username: String;
  password: String;
  data: String;
  
  private shared: SharedService;
  message = "{{username}}";

  constructor(private fb: FormBuilder) {
    this.createForm();
   }
   createForm() {
    this.angForm = this.fb.group({
       name: ['', Validators.required ],
       password: ['', Validators.required ]
    });
  }
  ngOnInit(): void {
    this.shared.setMessage(this.message)
  }

}
