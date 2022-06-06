import { AfterViewInit, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { faCrow } from '@fortawesome/free-solid-svg-icons';
import { faMapSigns } from '@fortawesome/free-solid-svg-icons';
import { faSkullCrossbones } from '@fortawesome/free-solid-svg-icons';
import { faArrowAltCircleUp } from '@fortawesome/free-solid-svg-icons';
import { faEllipsisH } from '@fortawesome/free-solid-svg-icons';
import { faUserAlt } from '@fortawesome/free-solid-svg-icons';
import { faCalendarDay } from '@fortawesome/free-solid-svg-icons';
import { faRoute } from '@fortawesome/free-solid-svg-icons';
import { faTrophy } from '@fortawesome/free-solid-svg-icons';
import { faScroll } from '@fortawesome/free-solid-svg-icons';
import { faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
import { AuthService } from 'src/app/core/services';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'] 
})
export class HeaderComponent implements OnInit, AfterViewInit {
  darkMode = false; 
  faCrow = faCrow;
  faSignOutAlt = faSignOutAlt;
  faTrophy = faTrophy;
  faScroll = faScroll;
  faRoute = faRoute;
  faCalendarDay = faCalendarDay;
  faMapSigns = faMapSigns;
  faSkullCrossbones = faSkullCrossbones;
  faArrowAltCircleUp = faArrowAltCircleUp;
  faEllipsisH = faEllipsisH;
  faUserAlt = faUserAlt;
  constructor(private authService : AuthService, public router: Router) { }

  ngOnInit(): void {
  }
  ngAfterViewInit(){
  }
  changeStyleMode(isDarkMode : any){
    this.darkMode = isDarkMode;
    const body = document.getElementById('body');
    body.classList.toggle("dark");
  }
  toggle(){
    const burgerButton = document.querySelectorAll('.navbar-burger').forEach((value)=>{
      value.classList.toggle('is-active');
    });
    document.getElementById('navMenu').classList.toggle('is-active')
  }

  logOut() {
    this.authService.logout();
    this.router.navigate(['./authentification']);
  }
}
