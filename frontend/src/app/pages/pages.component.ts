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
        const urlShortOld = this.currentUrl.split('(')[0]
        const urlShortNew = this.router.url.split('(')[0]
        if (this.currentUrl === '' || (this.router.url !== this.currentUrl && urlShortOld !== urlShortNew)) {
          this.currentUrl = this.router.url
          switch(this.currentUrl.split('(')[0]){
            case '/index':
              this.currentPanel = 'global-tutorial'
              break;
            case '/expeditions':
              this.currentPanel = 'expedition-tutorial'
            case '/aviary':
              this.currentPanel = 'aviary-tutorial'
              break;
            case '/attack':
              this.currentPanel = 'attack-tutorial'
              break;
            case '/upgrade':
              this.currentPanel = 'upgrade-tutorial'
              break;
            case '/adventure':
              this.currentPanel = 'adventure-tutorial'
              break;
            default:
              this.currentPanel = 'global-tutorial'
              break;
          }
        }
      }
    })
  }
  openTutorial(){
    this.modal.toggleModal();
  }
  changePanel(panel:string){
    this.currentPanel = panel
    console.log(this.currentPanel)
  }
}
