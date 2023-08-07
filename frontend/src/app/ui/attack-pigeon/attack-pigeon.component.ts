import { Component, Input } from '@angular/core';
import { Pigeon } from 'src/app/core/models';

@Component({
  selector: 'app-attack-pigeon',
  templateUrl: './attack-pigeon.component.html',
  styleUrls: ['./attack-pigeon.component.scss']
})
export class AttackPigeonComponent {
  @Input() pigeon: Pigeon

}
