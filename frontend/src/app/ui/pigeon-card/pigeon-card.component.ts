import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

import {
  faTree,
  faStar,
  faHatWizard,
  faFeatherAlt,
  faShieldAlt,
  faFistRaised,
  faPoop,
  faEgg,
  faHandPointer
} from '@fortawesome/free-solid-svg-icons';

import { Pigeon } from 'src/app/core/models/pigeon';

@Component({
  selector: 'app-pigeon-card',
  templateUrl: './pigeon-card.component.html',
  styleUrls: ['./pigeon-card.component.scss']
})
export class PigeonCardComponent implements OnInit {
  @Input() pigeon: Pigeon;
  @Output() sellPigeonEvent = new EventEmitter<Pigeon>();
  @Output() openCardEvent = new EventEmitter<Pigeon>();
  faTree = faTree;
  faStar = faStar;
  faHatWizard = faHatWizard;
  faFeatherAlt = faFeatherAlt;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faHandPointer = faHandPointer;
  faEgg = faEgg;
  faPoop = faPoop;
  luckStar: number;
  secondLeft: number;
  maxSecondLeft: number;
  pigeonType;
  classToApply: string;
  constructor() { }

  ngOnInit(): void {
    this.getPigeonType();
    this.luckStar = this.getStars();
    const activationDate = new Date(this.pigeon.active_time).getTime();
    const now = new Date().getTime();
    const creationTime = new Date(this.pigeon.creation_time).getTime();
    if (activationDate > now) {
      this.secondLeft = Math.ceil((activationDate - now) / 1000);
      this.maxSecondLeft = Math.ceil((activationDate - creationTime) / 1000);
      this.getTimeLeftBeforeActivation();
    }
  }

  getPigeonType() {
    switch (this.pigeon.pigeon_type) {
      case 1:
        this.pigeonType = faFistRaised;
        break;
      case 2:
        this.pigeonType = faHatWizard;
        break;
      case 3:
        this.pigeonType = faShieldAlt;
        break;
    }
  }

  sellPigeon() {
    this.sellPigeonEvent.emit(this.pigeon);
  }
  openCard() {
    this.openCardEvent.emit(this.pigeon);
  }
  getStars() {
    if (this.pigeon.luck > 93) {
      this.classToApply = 'legendary'
      return 5;
    } else if (this.pigeon.luck > 78) {
      this.classToApply = 'epic'
      return 4;
    } else if (this.pigeon.luck > 48) {
      this.classToApply = 'rare'
      return 3;
    } else if (this.pigeon.luck > 18) {
      this.classToApply = 'uncommon'
      return 2;
    } else {
      return 1;
    }
  }

  getTimeLeftBeforeActivation() {
    if (this.secondLeft > 0) {
      setTimeout(() => {
        this.secondLeft--;
        this.getTimeLeftBeforeActivation()
      }, 1000);
    }
  }
}
