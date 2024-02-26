import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdventureTutorialComponent } from './adventure-tutorial.component';

describe('AdventureTutorialComponent', () => {
  let component: AdventureTutorialComponent;
  let fixture: ComponentFixture<AdventureTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdventureTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdventureTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
