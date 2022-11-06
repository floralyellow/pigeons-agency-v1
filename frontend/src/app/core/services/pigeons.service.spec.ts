import { TestBed } from '@angular/core/testing';

import { PigeonsService } from './pigeons.service';

describe('PigeonsService', () => {
  let service: PigeonsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PigeonsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
