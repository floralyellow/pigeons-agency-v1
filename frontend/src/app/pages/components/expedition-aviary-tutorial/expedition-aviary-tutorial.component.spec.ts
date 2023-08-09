import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpeditionAviaryTutorialComponent } from './expedition-aviary-tutorial.component';

describe('ExpeditionAviaryTutorialComponent', () => {
  let component: ExpeditionAviaryTutorialComponent;
  let fixture: ComponentFixture<ExpeditionAviaryTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExpeditionAviaryTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExpeditionAviaryTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
