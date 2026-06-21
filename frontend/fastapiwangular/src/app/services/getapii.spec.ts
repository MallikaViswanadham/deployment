import { TestBed } from '@angular/core/testing';

import { Getapii } from './getapii';

describe('Getapii', () => {
  let service: Getapii;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Getapii);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
