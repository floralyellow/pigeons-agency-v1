import { ImplicitReceiver } from '@angular/compiler';
import { Component, OnChanges, OnInit } from '@angular/core';
import {PlayerService} from '../core/services/player.service'

@Component({
  selector: 'app-pages',
  templateUrl: './pages.component.html',
  styleUrls: ['./pages.component.scss']
})
export class PagesComponent implements OnInit {

  constructor(playerService : PlayerService ) {
    playerService
   }

  ngOnInit(): void {
  }
}
