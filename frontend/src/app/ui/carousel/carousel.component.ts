import { Component, Input } from '@angular/core';
import {
  faArrowAltCircleLeft,
  faArrowAltCircleRight
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.scss']
})
export class CarouselComponent {
  faArrowAltCircleLeft = faArrowAltCircleLeft
  faArrowAltCircleRight = faArrowAltCircleRight
  @Input() listItem : {
    src: string,
    description : string
  }[]
  currentIndex = 0

  previous(){
    this.currentIndex = (this.currentIndex === 0)? this.listItem.length - 1 : this.currentIndex - 1
  }

  next(){
    this.currentIndex = (this.currentIndex === this.listItem.length - 1)? 0 : this.currentIndex + 1
  }
}
