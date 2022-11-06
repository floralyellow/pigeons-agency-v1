import { Component, OnInit } from '@angular/core';
import { Adventure, Pigeon } from 'src/app/core/models';
import { AdventureService, PigeonsService } from 'src/app/core/services';

@Component({
  selector: 'app-adventure',
  templateUrl: './adventure.component.html',
  styleUrls: ['./adventure.component.scss']
})
export class AdventureComponent implements OnInit {
  currentAdventure: Adventure;
  adventurePigeons : Pigeon[];
  
  constructor(private adventureService : AdventureService) { }

  ngOnInit(): void {
    this.adventureService.getCurrentAdventure().then(result => {
      this.currentAdventure = result.adventure
      this.adventurePigeons = result.adventure_pigeons
    })
  }

}
