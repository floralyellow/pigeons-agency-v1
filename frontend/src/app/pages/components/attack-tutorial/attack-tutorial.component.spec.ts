import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttackTutorialComponent } from './attack-tutorial.component';

describe('AttackTutorialComponent', () => {
  let component: AttackTutorialComponent;
  let fixture: ComponentFixture<AttackTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AttackTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AttackTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
