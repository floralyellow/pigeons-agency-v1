import { Component, OnInit } from '@angular/core';
import { Expedition, Player } from 'src/app/core/models';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';

@Component({
  selector: 'app-aviary',
  templateUrl: './aviary.component.html',
  styleUrls: ['./aviary.component.scss']
})
export class AviaryComponent implements OnInit {
  pigeons: Pigeon[];
  info: Expedition;
  player: Player;
  seeds:number;
  constructor(private pigeonService: ExpeditionsService) {
    pigeonService.getExpeditionInfo().then((value : Expedition) => {
      this.pigeons = value.expeditions;
      this.info = value;
      this.player = value.user.player;
      this.seeds = this.player.seeds;
    })
   }

  ngOnInit(): void {
  }

}
