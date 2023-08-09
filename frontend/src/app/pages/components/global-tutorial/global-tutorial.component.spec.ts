import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GlobalTutorialComponent } from './global-tutorial.component';

describe('GlobalTutorialComponent', () => {
  let component: GlobalTutorialComponent;
  let fixture: ComponentFixture<GlobalTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GlobalTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GlobalTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
