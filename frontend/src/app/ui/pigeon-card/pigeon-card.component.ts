import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { faTree } from '@fortawesome/free-solid-svg-icons';
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { faMagic } from '@fortawesome/free-solid-svg-icons';
import { faFeatherAlt } from '@fortawesome/free-solid-svg-icons';
import { faShieldAlt } from '@fortawesome/free-solid-svg-icons';
import { faFistRaised } from '@fortawesome/free-solid-svg-icons';
import { faRunning } from '@fortawesome/free-solid-svg-icons';
import { faPoop } from '@fortawesome/free-solid-svg-icons';
import { faEgg } from '@fortawesome/free-solid-svg-icons';
import { Pigeon } from 'src/app/core/models/pigeon';

@Component({
  selector: 'app-pigeon-card',
  templateUrl: './pigeon-card.component.html',
  styleUrls: ['./pigeon-card.component.scss']
})
export class PigeonCardComponent implements OnInit {
  @Input() pigeon : Pigeon;
  @Output() sellPigeonEvent = new EventEmitter<Pigeon>();
  @Output() openCardEvent = new EventEmitter<Pigeon>();
  faTree = faTree;
  faStar = faStar;
  faMagic = faMagic;
  faFeatherAlt = faFeatherAlt;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faRunning = faRunning;
  faEgg = faEgg;
  faPoop = faPoop;
  luckStar: number;
  classToApply : string;
  constructor() { }

  ngOnInit(): void {
    this.luckStar = this.getStars();
  }

  sellPigeon(){
    this.sellPigeonEvent.emit(this.pigeon);
  }
  openCard(){
    this.openCardEvent.emit(this.pigeon);
  }
  getStars(){
    if(this.pigeon.luck > 93){
      this.classToApply = 'legendary'
      return 5;
    }else if(this.pigeon.luck > 78){
      this.classToApply = 'epic'
      return 4;
    }else if(this.pigeon.luck > 48){
      this.classToApply = 'rare'
      return 3;
    }else if(this.pigeon.luck > 18){
      this.classToApply = 'uncommon'
      return 2;
    }else{
      return 1;
    }
  }
}
