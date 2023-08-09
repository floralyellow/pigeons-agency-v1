import { Component, ViewChild } from '@angular/core';

import {
  faInfoCircle
} from '@fortawesome/free-solid-svg-icons';
import { ModalComponent } from '../ui';


@Component({
  selector: 'app-pages',
  templateUrl: './pages.component.html',
  styleUrls: ['./pages.component.scss']
})
export class PagesComponent {
  faInfoCircle = faInfoCircle
  modalTitle: string;
  modalContent: string;
  modalHeaderBackground: string;
  @ViewChild(ModalComponent) modal;
  openTutorial(){
    this.modal.toggleModal();
  }
}
