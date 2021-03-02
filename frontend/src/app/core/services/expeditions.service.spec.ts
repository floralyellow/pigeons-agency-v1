import { TestBed } from '@angular/core/testing';

import { ExpeditionsService } from './expeditions.service';

describe('ExpeditionsService', () => {
  let service: ExpeditionsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ExpeditionsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
