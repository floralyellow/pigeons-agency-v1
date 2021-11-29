import { Component, OnInit } from '@angular/core';
import { LeaderboardService } from 'src/app/core/services';
import { User } from 'src/app/core/models/user';

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.scss']
})
export class LeaderboardComponent implements OnInit {
  userList : User[];
  me : User;
  constructor(private leaserboardService : LeaderboardService) { }

  ngOnInit(): void {
    this.leaserboardService.getLeaderboard().then(value => {
      this.userList = value.users
      this.me = value.user
    });
  }

}
