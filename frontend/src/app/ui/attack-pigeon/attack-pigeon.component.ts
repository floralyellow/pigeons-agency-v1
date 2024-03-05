import { Component, Input } from '@angular/core';
import { Pigeon } from 'src/app/core/models';
import { PigeonsService } from 'src/app/core/services';

@Component({
  selector: 'app-attack-pigeon',
  templateUrl: './attack-pigeon.component.html',
  styleUrls: ['./attack-pigeon.component.scss']
})
export class AttackPigeonComponent {
  @Input() pigeon: Pigeon
  classToApply: "legendary" | "epic" | "rare" | "uncommon" | ""

  constructor(private pigeonService : PigeonsService) { }

  ngOnInit(): void {
    this.classToApply = this.pigeonService.getClassToApply(this.pigeon)
  }
}
