import { Component, Input, OnInit } from '@angular/core';
import { faTree } from '@fortawesome/free-solid-svg-icons';
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { faMagic } from '@fortawesome/free-solid-svg-icons';
import { faFeatherAlt } from '@fortawesome/free-solid-svg-icons';
import { faShieldAlt } from '@fortawesome/free-solid-svg-icons';
import { faFistRaised } from '@fortawesome/free-solid-svg-icons';
import { faRunning } from '@fortawesome/free-solid-svg-icons';
import { faPoop } from '@fortawesome/free-solid-svg-icons';
import { Pigeon } from 'src/app/core/models/pigeon';

@Component({
  selector: 'app-pigeon-card',
  templateUrl: './pigeon-card.component.html',
  styleUrls: ['./pigeon-card.component.scss']
})
export class PigeonCardComponent implements OnInit {
  @Input() pigeon : Pigeon;
  faTree = faTree;
  faStar = faStar;
  faMagic = faMagic;
  faFeatherAlt = faFeatherAlt;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faRunning = faRunning;
  faPoop = faPoop;
  constructor() { }

  ngOnInit(): void {
  }

}
