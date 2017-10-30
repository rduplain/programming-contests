## Solutions to practice programming contest problems.

A discussion at [beCamp](http://becamp.org) 2017 in Charlottesville, VA, USA,
led to a small informal group interested in practicing competitive programming.

Use local man pages only. Do not search the web.


### Problems

* [Kattis Problem Archive](https://open.kattis.com/)


### Guidance

Guidance on how to get started or advance in competitive programming are widely
discussed. Guidance here is on how competitive programming differs from
professional programming (or software as craft) and other topics on the mindset
of competitive programming.

* **Test using file I/O exclusively.** Automated systems accept program
  submissions and run them against secret test cases, first compiling the
  program as needed. Naturally, these systems use stdio so that the submitted
  program is a black box.
* **Test locally using the provided samples.** A problem typically includes
  sample input and output. Test using these.
* **Pass around a file descriptor.** Unless there's a reason to read the entire
  file into memory, typically problems are laid out line by line, and the
  program should read line by line accordingly. Specifically, professional
  programmers often push I/O and other integration details to the edges of the
  program.
* **The acceptance tests are like a frustrated user.** They complain loudly and
  don't provide any detail on what is wrong. For harder problems, add test
  cases beyond the samples provided.
* **Factor. Factor. Factor.** Who says programming doesn't involve math? Break
  the problem down, and when the solution is stuck, look for a different way to
  break it down.
* **Expect edge cases.** Counterintuitively, however, if a program is full of
  exceptional edge cases, then the solution is likely down the wrong
  path. Catch this early, revisit the problem, and go back to factoring.
* **Solutions need not be purely numeric.** Most solutions involve text or
  numeric processing, but there are times when the problem is readily addressed
  through a simulation in which the program searches a solution domain step by
  step, catching or pruning invalid combinations.
* **Lookups are often not an option.** Problems in the "real world" can include
  a pre-computed index which allow for quick search or lookup. Contest problems
  often specify input sizes which make it impractical to start the program by
  first computing an index.
* **Teams matter.** ... because the hard problems will take more time to
  complete than is scheduled for a contest.
* **Languages are limited.** A Lisp is probably not an option, unless supported
  by the platform accepting submissions, which is unlikely because the platform
  needs to compile and run the program submission in a prebuilt sandbox.
  Further, without internet access, programs will not be able to load libraries
  or embedded interpreters unless the team types these out, which is only a
  valid option for small libraries. Even then, solutions are independent so
  there's no harm in copy/paste, which is something to avoid in professional
  programming.
* **Python 3 does not have a maximum integer size.** [There is no limit to the
  value of integers in Python 3][Python 3 Integers], which makes it productive
  for problems where the primary challenge is handling very large values.
* **Notes and example solutions are valuable.** Without the web, notes and
  examples will speed up development by referring to concise, syntactically
  valid programs. If a solution has valid pseudocode, then it can be matched to
  actual code snippets.

[Python 3 Integers]: https://docs.python.org/3/whatsnew/3.0.html#integers
