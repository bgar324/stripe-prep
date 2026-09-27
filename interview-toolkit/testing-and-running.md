# HackerRank testing cheat sheet

You do not need your own IDE, terminal commands, a test framework, or debugger setup.

Use this for prep. Get approval before using AI-generated notes during the interview.

## 1. Run the example early

- Keep the supplied function name and parameters.
- Return the answer if the prompt asks for a return value. Printing is not a substitute.
- Click Run after implementing the first part. Read the result, not just whether execution finished.
- Run again after each follow-up.

If HackerRank provides tests or a driver that calls your function, use them. Enter custom input in the format that driver expects.

If it is a blank collaborative editor, call your function below its definition. Defining a function alone does not execute it.

## 2. Check three things

1. **Example:** does the complete output match the prompt?
2. **Boundary:** what happens exactly at the limit, and just beyond it?
3. **State or another branch:** does a rejected operation leave state unchanged? Do two different IDs stay independent?

Add empty input, duplicates, or ties when relevant. You do not need every imaginable edge case.

Say what you are testing: "The balance is 100. I'll try a payment of 101, then 100, to check that the rejected payment didn't change the balance."

## 3. Use an assertion if you need your own check

Store your function's return value in `actual`. Set `expected` to the answer you worked out by hand. Then run:

```python
assert actual == expected, f"expected {expected!r}, got {actual!r}"
print("Passed")
```

A match prints `Passed`. A mismatch raises `AssertionError` and shows both values. If the platform already compares outputs, you do not need this snippet.

Compare the whole result. Do not sort lists unless output order is irrelevant.

## 4. When it fails

- Read the error message and the indicated line.
- For a wrong answer, compare expected versus actual.
- Use a temporary `print()` to inspect the relevant variable or state before the wrong step.
- Fix the cause, then rerun the failing case and the earlier examples.
- Remove debug prints before the final run, especially if stdout is graded.

## Before interview day

Try HackerRank's sandbox once: select Python, run a function, deliberately trigger an assertion failure, and find the output/error panel. That is the environment practice you need.
