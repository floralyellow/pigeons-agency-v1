import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttackPigeonComponent } from './attack-pigeon.component';

describe('AttackPigeonComponent', () => {
  let component: AttackPigeonComponent;
  let fixture: ComponentFixture<AttackPigeonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AttackPigeonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AttackPigeonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
