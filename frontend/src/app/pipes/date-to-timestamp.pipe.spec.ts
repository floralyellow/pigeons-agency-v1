import { DateToTimestampPipe } from './date-to-timestamp.pipe';

describe('DateToTimestampPipe', () => {
  it('create an instance', () => {
    const pipe = new DateToTimestampPipe();
    expect(pipe).toBeTruthy();
  });
});
