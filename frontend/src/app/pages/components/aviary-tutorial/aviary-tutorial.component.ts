import { Component } from '@angular/core';

import { 
  faHatWizard,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-tutorial',
  templateUrl: './aviary-tutorial.component.html',
  styleUrls: ['./aviary-tutorial.component.scss']
})
export class AviaryTutorialComponent {
  faHatWizard = faHatWizard
  faShieldAlt = faShieldAlt
  faFistRaised = faFistRaised
}
