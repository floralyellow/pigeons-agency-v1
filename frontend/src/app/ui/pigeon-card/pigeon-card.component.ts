import { Component, OnInit } from '@angular/core';
import { faTree } from '@fortawesome/free-solid-svg-icons';
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { faHeart } from '@fortawesome/free-solid-svg-icons';
import { faFeatherAlt } from '@fortawesome/free-solid-svg-icons';
import { faShieldAlt } from '@fortawesome/free-solid-svg-icons';
import { faFistRaised } from '@fortawesome/free-solid-svg-icons';
import { faRunning } from '@fortawesome/free-solid-svg-icons';
import { faPoop } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-pigeon-card',
  templateUrl: './pigeon-card.component.html',
  styleUrls: ['./pigeon-card.component.scss']
})
export class PigeonCardComponent implements OnInit {

  faTree = faTree;
  faStar = faStar;
  faHeart = faHeart;
  faFeatherAlt = faFeatherAlt;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faRunning = faRunning;
  faPoop = faPoop;
  constructor() { }

  ngOnInit(): void {
  }

}
