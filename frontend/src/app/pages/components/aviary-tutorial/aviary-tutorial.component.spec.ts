import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AviaryTutorialComponent } from './aviary-tutorial.component';

describe('AviaryTutorialComponent', () => {
  let component: AviaryTutorialComponent;
  let fixture: ComponentFixture<AviaryTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AviaryTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AviaryTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
