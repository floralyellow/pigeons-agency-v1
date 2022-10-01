import { TestBed } from '@angular/core/testing';

import { IsNotAuth } from './is-not-auth.guard';

describe('IsNotAuthGuard', () => {
  let guard: IsNotAuth;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(IsNotAuth);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
