import { Component, Input, OnInit } from '@angular/core';
import { Pigeon } from 'src/app/core/models/pigeon';

@Component({
  selector: 'app-expedition-cooldown',
  templateUrl: './expedition-cooldown.component.html',
  styleUrls: ['./expedition-cooldown.component.scss']
})
export class ExpeditionCooldownComponent implements OnInit {
  @Input() pigeon : Pigeon;
  constructor() { }
  duration : number;
  timeLeft : number;
  ngOnInit(): void {
     this.duration = (new Date(this.pigeon.active_time).getTime() - new Date(this.pigeon.creation_time).getTime()) / 1000;
     this.timeLeft = (new Date(this.pigeon.active_time).getTime() - new Date(Date.now()).getTime())/1000;
  }

}
