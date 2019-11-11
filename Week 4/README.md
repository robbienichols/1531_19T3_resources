# Tutorial 4

## A. Acceptance Criteria

Take your user stories from the last tutorial and, as a class, assign some acceptance criteria. Consider how easy it would be to test them (either automatically or manually) and whether they sufficiently cover the requirements.

## B. Verification & Validation

Given the Zune bug example from the lecture (in `day_to_year.py`) and a test that **doesn't** find the bug (in `day_to_year_test.py`), fix the implementation of `day_to_year()` such that it no longer has the bug.

To check whether you have in fact removed the bug and that your tests are adequate, use Coverage.Py to measure and inspect your code coverage. You may need to add more to the test to have satisfactory coverage. Make sure you're doing **branch** coverage checking!

Run your `day_to_year.py` through pylint. Consider what issues it highlights and discuss, as a class, the alternatives for resolving them.

* Fixing the code so the issue no longer exists.
* Adding a pragma to the line the issue occurs, so pylint stops reporting it.
* Suppressing all instances of such errors via a config file.

You may wish to consult the [Google python style guide](https://google.github.io/styleguide/pyguide.html)

## C. Duck typing

Consider a simple number guessing game: a game master picks a number between 1 and 100 and the players each make a guess what that number is. Create classes for two kinds of players for this game. Human players are given all the numbers guessed so far and are asked (via the terminal) for their guess. "AI" players are also given all the numbers guessed so far, but make a guess by randomly choosing a number from the set of numbers that have not been guessed.

After implementing these two classes, write a function that takes in a list of players, "AI" or human, and uses duck typing to play the game.

**HINT:** You wil find the `random` module useful.

## D. Iterators

Write an iterator that generates all the fibonacci numbers less than 1000. Using a `for` loop, print out all those numbers.
