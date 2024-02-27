# Simple Guidelines

For all feature related work, it would be great to ask yourself the following questions before submitting a PR:

1. Is your code correct? Proof of correctness and at least one Python side test. It is ok to test against well-known packages. Don't forget to add to requirements-test.txt if more packages need to be downloaded for tests.
2. Are you using a lot of unwraps in your code? Are these unwraps justified? Same for unsafe code.
3. If an additional dependency is needed, how much of it is really used? Will it bloat the package? What other features can we write with the additional dependency? I would discourage add an dependency if we are using 1 or 2 function out of that package.
4. Everything can be discussed. 


## Remember to run these before committing:
1. pre-commit. We use ruff.
2. cargo fmt