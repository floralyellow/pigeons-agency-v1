import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../core/services/auth.service'

@Component({
  selector: 'app-authentification',
  templateUrl: './authentification.component.html',
  styleUrls: ['./authentification.component.scss']
})
export class AuthentificationComponent implements OnInit {
  login={
    username:"",
    password:""
  }
  register={
    username:"",
    password:""
  }
  constructor(public router: Router,private authService : AuthService) { }

  ngOnInit(): void {
  }
  async submit( type : string ){
    if (type === 'register'){
      await this.authService.register
      ({
        username : this.register.username,
        password : this.register.password
      })
    }else{
      await this.authService.login
      ({
        username : this.login.username,
        password : this.login.password
      }).then(()=>{
        this.router.navigate(['/index']);
      });

    }
  }
}
