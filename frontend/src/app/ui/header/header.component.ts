import { Component, Input, OnInit } from '@angular/core';
import { faCrow } from '@fortawesome/free-solid-svg-icons';
import { faMapSigns } from '@fortawesome/free-solid-svg-icons';
import { faSkullCrossbones } from '@fortawesome/free-solid-svg-icons';
import { Player } from 'src/app/core/models/player';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'] 
})
export class HeaderComponent implements OnInit {
  //@Input() player : Player;
  darkMode = false; 
  faCrow = faCrow;
  faMapSigns = faMapSigns;
  faSkullCrossbones = faSkullCrossbones;
  constructor() { }

  ngOnInit(): void {
  }

  changeStyleMode(isDarkMode : any){
    this.darkMode = isDarkMode;
    const body = document.getElementById('body');
    body.classList.toggle("dark");
  }
}
