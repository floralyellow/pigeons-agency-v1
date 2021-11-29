import { TestBed } from '@angular/core/testing';

import { UpgradeService } from './upgrade.service';

describe('UpgradeService', () => {
  let service: UpgradeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UpgradeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
