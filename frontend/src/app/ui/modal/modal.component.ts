import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss']
})
export class ModalComponent {
  @Input() title: string;
  @Input() headerBackground: string;
  isModalShown = false;

  toggleModal() {
    this.isModalShown = !this.isModalShown
  }
}
