import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpgradeTutorialComponent } from './upgrade-tutorial.component';

describe('UpgradeTutorialComponent', () => {
  let component: UpgradeTutorialComponent;
  let fixture: ComponentFixture<UpgradeTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UpgradeTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UpgradeTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
