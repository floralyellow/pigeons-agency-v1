import { TestBed } from '@angular/core/testing';

import { AttackService } from './attack.service';

describe('AttackService', () => {
  let service: AttackService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AttackService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
