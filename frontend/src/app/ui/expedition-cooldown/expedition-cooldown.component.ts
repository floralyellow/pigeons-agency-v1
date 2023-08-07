import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { Pigeon } from 'src/app/core/models/pigeon';

@Component({
  selector: 'app-expedition-cooldown',
  templateUrl: './expedition-cooldown.component.html',
  styleUrls: ['./expedition-cooldown.component.scss']
})
export class ExpeditionCooldownComponent implements OnInit, OnDestroy {
  @Input() pigeon: Pigeon;
  constructor() { }
  duration: number;
  timeLeft: number;
  timeout
  ngOnInit(): void {
    const activeTime = new Date(this.pigeon.active_time).getTime();
    const creationTime = new Date(this.pigeon.creation_time).getTime();
    const now = new Date(Date.now()).getTime();
    this.duration = (
      activeTime - creationTime
    ) / 1000;
    this.getTimeLeft()
  }
  ngOnDestroy(): void {
    clearTimeout(this.timeout)
  }
  getTimeLeft() {
    this.timeLeft = Math.round(
      ((new Date(this.pigeon.active_time).getTime() - new Date(Date.now()).getTime()
      ) / 1000) - 1);
    if (new Date(this.pigeon.active_time).getTime() > new Date(Date.now()).getTime()) {
      this.timeout = setTimeout(() => {
        this.timeLeft = Math.round(
          ((new Date(this.pigeon.active_time).getTime() - new Date(Date.now()).getTime()
          ) / 1000) - 1);
        this.getTimeLeft();
      }, 1000);
    }
    else {
      this.timeLeft = 0;
      clearTimeout(this.timeout)
    }
  }
}
