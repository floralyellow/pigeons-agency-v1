import { Component, Input } from '@angular/core';
@Component({
  selector: 'app-expedition-card',
  templateUrl: './expedition-card.component.html',
  styleUrls: ['./expedition-card.component.scss']
})
export class ExpeditionCardComponent  {
  @Input() info: {
    name: string,
    duration: number,
    seeds: number
  };

}
