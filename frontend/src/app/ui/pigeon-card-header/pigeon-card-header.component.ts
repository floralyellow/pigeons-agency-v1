import { Component, Input, OnInit } from '@angular/core';
import { Pigeon } from 'src/app/core/models/pigeon';
import { PigeonsService } from 'src/app/core/services/';

import {
  faStar,
  faHatWizard,
  faFeatherAlt,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';



@Component({
  selector: 'app-pigeon-card-header',
  templateUrl: './pigeon-card-header.component.html',
  styleUrls: ['./pigeon-card-header.component.scss']
})
export class PigeonCardHeaderComponent implements OnInit {
  @Input() pigeon: Pigeon;
  @Input() size: string;

  faStar = faStar;

  faHatWizard = faHatWizard;
  faFeatherAlt = faFeatherAlt;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;

  pigeonTypes = {
    'faHatWizard' : faHatWizard,
    'faShieldAlt' : faShieldAlt,
    'faFistRaised' : faFistRaised
  };
  pigeonType;
  classToApply: string;
  luckStar;

  constructor(private pigeonsService : PigeonsService) { }

  ngOnInit(): void {
    this.pigeonType = this.pigeonTypes[this.pigeonsService.getPigeonType(this.pigeon)];
    this.luckStar = this.pigeonsService.getStars(this.pigeon);
  }
}
