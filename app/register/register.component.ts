import { Component, OnInit } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent{
  title = 'Machine Learning Future Prediction';
  angForm: FormGroup;
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
  }

}
