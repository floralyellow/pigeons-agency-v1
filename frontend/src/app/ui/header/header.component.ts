import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'] 
})
export class HeaderComponent implements OnInit {
  darkMode = false; 
  constructor() { }

  ngOnInit(): void {
  }

  changeStyleMode(isDarkMode : any){
    this.darkMode = isDarkMode;
    const body = document.getElementById('body');
    body.classList.toggle("dark");
  }
}
