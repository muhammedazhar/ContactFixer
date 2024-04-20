- it should remove the character [U+202D] which is a Unicode character known as the "Left-to-Right Override" (LRO).
- I think I wish to add a single white space ' ' between 5 digits like the following.


Here are the mobile number formats for different countries in list format, with two spaces used effectively:

1. USA: +1 (123) 456 7890
2. UK: +44 7123 456789
3. India: +91 98765 43210
4. UAE: +971 50 123 4567
5. Qatar: +974 3333 4444
6. Canada: +1 (416) 123 4567
7. New Zealand: +64 21 123 4567
8. Australia: +61 4 1234 5678
9. Latvia: +371 2345 6789
10. Ukraine: +380 67 123 4567

- When a number value contains the delimiter symbol ':::' between two phone numbers which doesn't have country code in it, the function doesn't get applied. 

Example:
8547807211 ::: 8848490020
99466 88887 ::: 90741 60693