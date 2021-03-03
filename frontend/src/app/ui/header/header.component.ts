import { AfterViewInit, Component, Input, OnInit } from '@angular/core';
import { faCrow } from '@fortawesome/free-solid-svg-icons';
import { faMapSigns } from '@fortawesome/free-solid-svg-icons';
import { faSkullCrossbones } from '@fortawesome/free-solid-svg-icons';
import { Player } from 'src/app/core/models/player';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'] 
})
export class HeaderComponent implements OnInit, AfterViewInit {
  //@Input() player : Player;
  darkMode = false; 
  faCrow = faCrow;
  faMapSigns = faMapSigns;
  faSkullCrossbones = faSkullCrossbones;
  constructor() { }

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
      /*burgerButton.map((value : Element)=>{
        value.toggleClass("is-active");
      })
      $(".navbar-menu").toggleClass("is-active");*/

  }
}
