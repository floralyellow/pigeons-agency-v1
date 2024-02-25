import { Component, OnInit } from '@angular/core';
import { LeaderboardService } from 'src/app/core/services';
import { User } from 'src/app/core/models/user';

import {
  faMedal,
  faAward,
  faTrophy
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.scss']
})
export class LeaderboardComponent implements OnInit {
  userList : User[];
  me : User;
  faMedal = faMedal;
  faTrophy = faTrophy;
  faAward = faAward;
  constructor(private leaserboardService : LeaderboardService) { }

  ngOnInit(): void {
    this.leaserboardService.getLeaderboard().then(value => {
      this.userList = value.users
      this.me = value.user
    });
  }

}
