import { ImplicitReceiver } from '@angular/compiler';
import { Component, OnChanges, OnInit } from '@angular/core';
import { Player } from '../core/models/player';
import {PlayerService} from '../core/services/player.service'

@Component({
  selector: 'app-pages',
  templateUrl: './pages.component.html',
  styleUrls: ['./pages.component.scss']
})
export class PagesComponent implements OnInit {
  player : Player;
  constructor(playerService : PlayerService ) {
    playerService.getPlayerInfo().then((value : Player) => {
      this.player = value;
    })
   }

  async ngOnInit() {
  }
}
