# Mock Reasoning Report — Group <NN>

192-211 Automated Software Testing · Siam University

Fill in every field. Keep the question numbers. Paste output as text inside the
fenced blocks. Delete nothing from this template.

## Group members

| # | Student ID | Name | GitHub username | Experiments run |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

Every member must appear in `git shortlog -sn` with at least one commit.


---

## Part 0: Setup (required before any question)

### Q0.1

*Run `pytest -q` and paste the full summary line. State how many tests passed and how long the whole suite took.*

**Answer:**



### Q0.2

*Nothing in this suite reads a file, opens a socket, or sleeps. Using your timing from Q0.1, estimate how long these eight tests would take if each one contacted its real dependency over a network. State the assumption behind your estimate.*

**Answer:**




---

## Example 1: `return_value`

### Q1.1

*State the behaviour this test verifies in one sentence, then state one behaviour a reader might assume it verifies but which it does not.*

**Answer:**



### Q1.2

*The number 25 appears twice, once in the setup and once in the assertion. Explain what is actually being compared, and explain why a test that asserts a value it supplied itself is still worth writing here.*

**Answer:**



### Q1.3

*Suppose the test called the real weather API. List three distinct ways that test could fail on a day when `WeatherService` contains no defect at all. For each one, say whether a developer looking at the red test would be able to tell it was not their fault.*

**Answer:**



### Q1.4

*`Mock()` creates attributes on demand. Explain, from the pasted output of Experiment 1A, what this means for a test that contains a spelling mistake.*

**Answer:**



### Experiment 1A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q1.5

*The two tests fail for different reasons. Quote the two error messages and explain which of the two tells a developer where the real mistake is. Say which form of mock you would require in your own project, and name one cost of that choice.*

**Answer:**




---

## Example 2: Verifying a Method Call

### Q2.1

*`login()` returns nothing. Explain what is left to assert on when a method has no return value, and why that forces a different style of test from Example 1.*

**Answer:**



### Q2.2

*`assert_called_once_with` checks three things at once. Name all three. Then describe a defect in `login()` that each one would catch and the other two would miss.*

**Answer:**



### Q2.3

*Logging is often called a side concern. Argue either that asserting on a log call is valuable, or that it is over-specification that will break on the next harmless wording change. Commit to one position and give a rule your group would follow.*

**Answer:**



### Experiment 2A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q2.4

*`test_misspelled_assertion` names a method that does not exist and asserts about the wrong user. Explain from the output what Python did with it, and whether the protection you observed would still apply to a misspelling such as `logger.inf.assert_called_once_with(...)`. Run that variant if you are not sure, and paste the result.*

**Answer:**



### Q2.5

*Replace the mock with a real `logging.Logger` writing to a file. Describe the steps the test would then need in order to make the same assertion. Count the lines and name the part most likely to fail on another machine.*

**Answer:**




---

## Example 3: Dependency Injection

### Q3.1

*Name the injected dependency and the exact line where the substitution becomes possible.*

**Answer:**



### Q3.2

*Rewrite `__init__` so that the gateway is constructed inside the class instead of being passed in. Then try to write a test for `send_code` against that version without touching the production code. Report how far you got and where you stopped.*

**Answer:**



### Q3.3

*This test asserts only on the returned string. Add `gateway.send.assert_called_once_with("0812345678", "1234")` and run it. Paste the result, then state what this second assertion reveals about `send_code` that the first one hides.*

**Answer:**



### Q3.4

*The verification code `"1234"` is fixed in the production code. Explain whether this is a defect, and explain why the existing test passes either way. State the smallest change to the test that would make the choice visible to a reviewer.*

**Answer:**



### Experiment 3A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q3.5

*Paste the output. The production code has not changed. Explain what this tells you about where the asserted value comes from, and what that means for how much confidence a passing run of this test should give you.*

**Answer:**




---

## Example 4: `side_effect` as a List

### Q4.1

*Replace `side_effect = [1, 2, 3]` with `return_value = 1` and run the test. Paste the failure. Explain from that output what property of the production code the list form is checking and the single form cannot.*

**Answer:**



### Q4.2

*Name two real dependencies that return a different value on each call, and one that is expected to return the same value every time. Say which of `side_effect` and `return_value` fits each, and why.*

**Answer:**



### Q4.3

*The assertion compares a list, so order matters. Describe a defect in `create_three_ids` that produces the right three values in the wrong order, and say whether this test would catch it.*

**Answer:**



### Experiment 4A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q4.4

*Name the exception raised on the fourth call. Explain why this is useful feedback rather than a nuisance, and describe the change in production code that would cause a real test suite to start failing this way.*

**Answer:**




---

## Example 5: `side_effect` as an Exception

### Q5.1

*Describe, as a procedure another student could follow, how you would make a real disk return "no space left" on demand. Then estimate the time and the risk of doing that on the machine you are working on now.*

**Answer:**



### Q5.2

*This test proves the failure path returns `"FAILED"`. Name one thing the function should arguably also do when a write fails, and explain why this test passing says nothing about it.*

**Answer:**



### Q5.3

*The `except` clause names `IOError`. Explain what happens to a storage backend that raises a different exception type, using the output from Experiment 5A as evidence.*

**Answer:**



### Experiment 5A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q5.4

*State the difference between a test that fails on its assertion and a test that fails because an exception escaped the code under test. Explain which one you observed here and how you could tell from the output alone.*

**Answer:**



### Q5.5

*Both a happy path and a failure path now exist for `save`. Write the missing happy-path test, run it, and paste the result. Explain why the failure test on its own was not enough evidence that `save` works.*

**Answer:**




---

## Example 6: `side_effect` as a Function

### Q6.1

*Explain what the mock receives, what it passes on, and what it returns. Then state what breaks if `total` forgets to pass `amount` through. Verify your claim by making that change and pasting the output.*

**Answer:**



### Q6.2

*A function was used here instead of a fixed value or a list. State the condition under which each of the three forms is the right choice. Give the rule in terms of the dependency's behaviour, not in terms of syntax.*

**Answer:**



### Q6.3

*The mock now contains arithmetic. Argue whether `add_tax` has become a second implementation that must itself be kept correct, and say what you would do if the real tax rule changed.*

**Answer:**



### Experiment 6A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q6.4

*The original test asserts `== 107` and passes. This one asserts `== 5.35` and does not. Explain the difference using the exact numbers pytest printed. State the change you would make to the assertion, and say whether that change hides a real defect or removes a false alarm.*

**Answer:**




---

## Example 7: `patch` as a Context Manager

### Q7.1

*In Examples 1 to 6 the dependency arrived through `__init__`. Here it does not. Explain what `report_name` depends on and why that dependency cannot be injected without editing the production code.*

**Answer:**



### Q7.2

*Write the file below, run `pytest -q -s exp_print_scope.py`, and paste both printed lines. Explain what the context manager did on entry and on exit.*

**Answer:**



### Q7.3

*State what would happen to the other tests in the suite if the replacement were not undone at the end of the block. Say whether the order in which pytest runs tests would then matter.*

**Answer:**



### Experiment 7A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q7.4

*One passes and one fails, and the two patch strings differ by one word. Explain what each string names, using the value printed in the failure message as your evidence. Then state the rule your group will use to choose a patch target, in a form that works for any module.*

**Answer:**



### Q7.5

*Explain why the original `test_date_utils.py` passes with `"date_utils.current_year"` even though `exp_patch_target.py` does not. Point to the difference in how each module obtained the name.*

**Answer:**




---

## Example 8: `patch` as a Decorator

### Q8.1

*Name what is replaced and for how long. Compare the lifetime of the replacement here with the lifetime in Example 7, and say which is easier to get wrong when a test file grows to twenty tests.*

**Answer:**



### Q8.2

*The test function takes a parameter `mock_name` that nothing in the test file calls it with. Explain where that argument comes from. Then delete the parameter, run the test, and paste the error.*

**Answer:**



### Q8.3

*Remove the decorator but keep the assertion, run it, and paste the failure. Explain what the message `Hello Real User` versus `Hello Alice` tells you about what patching actually changed.*

**Answer:**



### Experiment 8A

**Prediction, written before running** (pass or fail, and what message):

> 

**Command run:**

```

```

**Output, pasted as text:**

```

```

### Q8.4

*State the order in which stacked decorators bind to parameters, with the output as evidence. Say what a group should do to make this unmistakable to the next reader of the test.*

**Answer:**



### Q8.5

*Both the context manager and the decorator form replace the same function. Give one situation where you would choose each, in terms of the scope of the test rather than personal taste.*

**Answer:**




---

## Part 9: Synthesis

### Q9.1

*Every test in this assignment passes, and in every case the value being asserted was chosen by the test author. Explain what this class of test can establish about a program, and what it cannot. Be specific about which kind of defect survives a fully green mock-based suite.*

**Answer:**



### Q9.2

*Examples 1 to 6 receive their dependency as an argument. Examples 7 and 8 reach into a module to replace a name. State which of the two you would prefer in new code and why. Then state what you would do when the code is not yours to change.*

**Answer:**



### Q9.3

*For each of the eight examples, decide whether mocking was necessary, merely convenient, or arguably wrong. Present your verdicts in a table with a one-line reason each. A verdict of "mocking is not justified here" is a correct answer if you can defend it.*

**Answer:**



### Q9.4

*Pick the one experiment above whose result surprised your group most, and say what you now check for in your own tests because of it. If no result surprised you, say so and give the prediction you were most confident about and why.*

**Answer:**



---

## Checklist before submitting

- [ ] `pytest -q` in the repo root reports 8 passed.
- [ ] Every `exp_*.py` file named in the handout exists in the repo.
- [ ] Every prediction was written before its experiment was run.
- [ ] Every pasted block is text, not an image.
- [ ] Every member has at least one commit (`git shortlog -sn`).
- [ ] Exported to `MockReasoning_Group<NN>.pdf`.
