import { Component, Input, OnInit } from '@angular/core';
import { Expedition } from 'src/app/core/models';

@Component({
  selector: 'app-expedition-card',
  templateUrl: './expedition-card.component.html',
  styleUrls: ['./expedition-card.component.scss']
})
export class ExpeditionCardComponent implements OnInit {
  @Input() info:Expedition;
  constructor() { }

  ngOnInit(): void {
  }

}
