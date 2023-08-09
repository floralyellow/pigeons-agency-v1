import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import {
  faCrow,
  faMapSigns,
  faSkullCrossbones,
  faArrowAltCircleUp,
  faEllipsisH,
  faUserAlt,
  faCalendarDay,
  faRoute,
  faTrophy,
  faScroll,
  faSignOutAlt
} from '@fortawesome/free-solid-svg-icons';

import { AuthService, PlayerService } from 'src/app/core/services';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit{
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
  constructor(private authService: AuthService, public router: Router, private playerService : PlayerService) { }

  async ngOnInit() {
    const isDarkMode = (await this.playerService.getPlayerInfo()).user.player.is_dark_mode
    if (isDarkMode === true){
      (document.querySelector('#dark-mode') as HTMLInputElement).checked = true;
      this.darkModeStyle()
    }
  }

  changeStyleMode(isDarkMode: boolean) {
    this.playerService.setDarkMode().then(()=>{
      this.darkMode = isDarkMode;
      this.darkModeStyle()
    })
  }

  darkModeStyle(){
    const body = document.getElementById('body');
    body.classList.toggle("dark");
  }

  toggle() {
    const burgerButton = document.querySelectorAll('.navbar-burger').forEach((value) => {
      value.classList.toggle('is-active');
    });
    document.getElementById('navMenu').classList.toggle('is-active')
  }

  logOut() {
    this.authService.logout();
    this.router.navigate(['./authentification']);
  }
}
