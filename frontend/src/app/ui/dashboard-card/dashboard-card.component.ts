import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard-card',
  templateUrl: './dashboard-card.component.html',
  styleUrls: ['./dashboard-card.component.scss']
})
export class DashboardCardComponent implements OnInit {
  @Input() actuelNumber: number;
  @Input() maxNumber: number;
  @Input() title: string;

  constructor() { }

  ngOnInit(): void {
  }

}
