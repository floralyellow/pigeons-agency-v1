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
import { PigeonsService } from 'src/app/core/services';

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
  secondLeft: number;
  maxSecondLeft: number;
  classToApply: "legendary" | "epic" | "rare" | "uncommon" | ""
  
  constructor(private pigeonService : PigeonsService) { }

  ngOnInit(): void {
    const activationDate = new Date(this.pigeon.active_time).getTime();
    const now = new Date().getTime();
    const creationTime = new Date(this.pigeon.creation_time).getTime();
    this.classToApply = this.pigeonService.getClassToApply(this.pigeon)
    if (activationDate > now) {
      this.secondLeft = Math.ceil((activationDate - now) / 1000);
      this.maxSecondLeft = Math.ceil((activationDate - creationTime) / 1000);
      this.getTimeLeftBeforeActivation();
    }
  }

  sellPigeon() {
    this.sellPigeonEvent.emit(this.pigeon);
  }
  openCard() {
    this.openCardEvent.emit(this.pigeon);
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
