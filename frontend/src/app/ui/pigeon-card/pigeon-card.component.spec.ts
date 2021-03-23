import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PigeonCardComponent } from './pigeon-card.component';

describe('PigeonCardComponent', () => {
  let component: PigeonCardComponent;
  let fixture: ComponentFixture<PigeonCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PigeonCardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PigeonCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
