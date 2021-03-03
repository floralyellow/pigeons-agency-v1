import { Component, OnInit } from '@angular/core';
import { Expedition } from 'src/app/core/models/expedition';
import * as expeditionInfo from 'src/assets/jsons/tr_expedition.json';

@Component({
  selector: 'app-expeditions',
  templateUrl: './expeditions.component.html',
  styleUrls: ['./expeditions.component.scss']
})
export class ExpeditionsComponent implements OnInit {
  expeditionList:Expedition[] = (expeditionInfo as any).default;

  constructor() { }

  ngOnInit(): void { 
  }

}
