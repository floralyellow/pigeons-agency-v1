import { TestBed } from '@angular/core/testing';

import { IsAuth } from './is-auth.guard';

describe('IsAuthGuard', () => {
  let guard: typeof IsAuth;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(IsAuth);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
