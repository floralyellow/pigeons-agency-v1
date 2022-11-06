import { Component, Input, OnInit } from '@angular/core';
import { PigeonsService } from 'src/app/core/services/';

import {
  faStar,
  faHatWizard,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';
import { Pigeon } from 'src/app/core/models';

@Component({
  selector: 'app-adventure-card',
  templateUrl: './adventure-card.component.html',
  styleUrls: ['./adventure-card.component.scss']
})
export class AdventureCardComponent implements OnInit {
  @Input() pigeon : Pigeon

  faStar = faStar;
  faHatWizard = faHatWizard;
  faFistRaised = faFistRaised;
  faShieldAlt = faShieldAlt;
  classToApply: "legendary" | "epic" | "rare" | "uncommon" | ""

  constructor(private pigeonService : PigeonsService) { }

  ngOnInit(): void {
    this.classToApply = this.pigeonService.getClassToApply(this.pigeon)
  }

}
