# String Slicing

Up to three numbers separated by colons (`:`) within square brackets after a string give a *slice* of the string (a shorter string):
* The first number gives the *start* index of the slice.
* The second number gives the *stop* index. This is exclusive, so the slice includes character up to but not including the stop index.
* The third number gives the *step*. The index is advanced by this much for each character of the slice, so (for example) a step of 2 will include every other character. If the step is negative, the slice works backward from the start to (but not including) the stop.

Any or all of the three numbers specifying a slice may be omitted.
* If no step is provided, the slice starts at the beginning of the string.
  * ... unless the step is negative, in which case the slice starts at the end of the string.
* If no stop is provided, the slice stops at the end of the string.
  * ... unless the step is negative, in which case the slice stops at the beginning of the string.
* If no step is provided, a step of 1 is used. The second colon can be omitted in this case.

If the stop is beyond the end of the string, the slice ends where the string ends.
