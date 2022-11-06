import { TestBed } from '@angular/core/testing';

import { AdventureService } from './adventure.service';

describe('AdventureService', () => {
  let service: AdventureService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AdventureService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
