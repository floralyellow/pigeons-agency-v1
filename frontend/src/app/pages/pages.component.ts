import { Component, OnChanges, ViewChild } from '@angular/core';

import {
  faInfoCircle
} from '@fortawesome/free-solid-svg-icons';
import { ModalComponent } from '../ui';
import { NavigationEnd, Router } from '@angular/router';


@Component({
  selector: 'app-pages',
  templateUrl: './pages.component.html',
  styleUrls: ['./pages.component.scss']
})
export class PagesComponent {
  @ViewChild(ModalComponent) modal;
  faInfoCircle = faInfoCircle
  modalTitle: string;
  modalContent: string;
  modalHeaderBackground: string;
  currentUrl=''
  currentPanel=''
  constructor(private router: Router){
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        console.log(this.router.url)
        if (this.currentUrl === '' || this.router.url !== this.currentUrl) {
          this.currentUrl = this.router.url
          switch(this.currentUrl.split('(')[0]){
            case '/index':
              this.currentPanel = 'global-tutorial'
              break;
            case '/expeditions':
            case '/aviary':
              this.currentPanel = 'expedition-aviary-tutorial'
              break;
            case '/attack':
              this.currentPanel = 'attack-tutorial'
              break;
          }
        }
      }
    })
  }
  openTutorial(){
    this.modal.toggleModal();
  }
}
