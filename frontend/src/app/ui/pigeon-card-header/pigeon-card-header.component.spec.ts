import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PigeonCardHeaderComponent } from './pigeon-card-header.component';

describe('PigeonCardHeaderComponent', () => {
  let component: PigeonCardHeaderComponent;
  let fixture: ComponentFixture<PigeonCardHeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PigeonCardHeaderComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PigeonCardHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
