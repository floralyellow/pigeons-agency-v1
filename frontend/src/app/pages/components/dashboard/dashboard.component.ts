import { Component, Input, OnInit } from '@angular/core';
import { Player } from 'src/app/core/models/player';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  @Input() player : Player;
  constructor() { }

  ngOnInit(): void {
  }

}
