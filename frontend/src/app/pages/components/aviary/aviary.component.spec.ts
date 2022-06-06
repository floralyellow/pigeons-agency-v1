import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AviaryComponent } from './aviary.component';

describe('AviaryComponent', () => {
  let component: AviaryComponent;
  let fixture: ComponentFixture<AviaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AviaryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AviaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
