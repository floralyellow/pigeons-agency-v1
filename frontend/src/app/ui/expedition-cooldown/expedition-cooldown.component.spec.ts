import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpeditionCooldownComponent } from './expedition-cooldown.component';

describe('ExpeditionCooldownComponent', () => {
  let component: ExpeditionCooldownComponent;
  let fixture: ComponentFixture<ExpeditionCooldownComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExpeditionCooldownComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ExpeditionCooldownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
