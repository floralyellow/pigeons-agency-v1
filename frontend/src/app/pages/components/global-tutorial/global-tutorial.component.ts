import { Component } from '@angular/core';

@Component({
  selector: 'app-global-tutorial',
  templateUrl: './global-tutorial.component.html',
  styleUrls: ['./global-tutorial.component.scss']
})
export class GlobalTutorialComponent {
  test=[
    {
      src: "assets/pigeons/bombird_green.png",
      description:"<h1>Test 1</h1>"
    },
    {
      src: "assets/pigeons/bombird_black.png",
      description:"test 2"
    }
  ]
}
