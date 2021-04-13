# Lab 4: Coverage and Pydocstyle

## Coverage.
### Initial coverage results.
```
Name                 Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------
lab1\__init__.py         0      0      0      0   100%
lab1\convert_2x.py      18      0     10      0   100%
lab2\__init__.py         0      0      0      0   100%
lab2\converters.py      23      0     12      0   100%
lab2\profit.py          11      0      2      0   100%
lab3\__init__.py         0      0      0      0   100%
lab3\directory.py       55      0     12      1    99%   56->62
----------------------------------------------------------------
TOTAL                  107      0     36      1    99%
```
### Coverage results after adding tests for find_words() and find_numbers().
```
Name                  Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------
lab1\__init__.py          0      0      0      0   100%
lab1\convert_2x.py       17      0     10      0   100%
lab1\find_number.py      28      3      8      1    89%   19-21, 30->12
lab1\find_words.py       20      2     12      0    94%   16-17
lab2\__init__.py          0      0      0      0   100%
lab2\converters.py       23      0     12      0   100%
lab2\profit.py           11      0      2      0   100%
lab3\__init__.py          0      0      0      0   100%
lab3\directory.py        55      0     12      1    99%   65->71
-----------------------------------------------------------------
TOTAL                   154      5     56      2    97%
```
### Coverage results after attending missing column from report.
```
Name                  Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------
lab1\__init__.py          0      0      0      0   100%
lab1\convert_2x.py       17      0     10      0   100%
lab1\find_number.py      27      0      6      0   100%
lab1\find_words.py       20      0     12      0   100%
lab2\__init__.py          0      0      0      0   100%
lab2\converters.py       23      0     12      0   100%
lab2\profit.py           11      0      2      0   100%
lab3\__init__.py          0      0      0      0   100%
lab3\directory.py        55      0     12      0   100%
-----------------------------------------------------------------
TOTAL                   153      0     54      0   100%
```

## Pydocstyle.
### Initial pydocstyle results.
```
.\lab1\convert_2x.py:1 at module level:
        D100: Missing docstring in public module
.\lab1\convert_2x.py:4 in public function `decimal_to_base`:
        D103: Missing docstring in public function
.\lab1\convert_2x.py:14 in public function `decimal_to_bin`:
        D103: Missing docstring in public function
.\lab1\convert_2x.py:23 in public function `decimal_to_hex`:
        D103: Missing docstring in public function
.\lab1\find_number.py:1 at module level:
        D100: Missing docstring in public module
.\lab1\find_number.py:4 in public function `find_number`:
        D103: Missing docstring in public function
.\lab1\find_words.py:1 at module level:
        D100: Missing docstring in public module
.\lab1\find_words.py:8 in public function `find_words`:
        D103: Missing docstring in public function
.\lab1\__init__.py:1 at module level:
        D104: Missing docstring in public package
.\lab2\converters.py:1 at module level:
        D100: Missing docstring in public module
.\lab2\profit.py:1 at module level:
        D100: Missing docstring in public module
.\lab2\profit.py:4 in public class `ProfitScenario`:
        D101: Missing docstring in public class
.\lab2\__init__.py:1 at module level:
        D104: Missing docstring in public package
.\lab3\directory.py:1 at module level:
        D100: Missing docstring in public module
.\lab3\directory.py:10 in public class `Record`:
        D101: Missing docstring in public class
.\lab3\directory.py:17 in public method `__post_init__`:
        D105: Missing docstring in magic method
.\lab3\directory.py:21 in public class `Directory`:
        D101: Missing docstring in public class
.\lab3\directory.py:24 in public method `__init__`:
        D107: Missing docstring in __init__
.\lab3\directory.py:27 in public method `add_record`:
        D102: Missing docstring in public method
.\lab3\directory.py:35 in public method `delete_record`:
        D102: Missing docstring in public method
.\lab3\directory.py:52 in public method `look_for_record`:
        D102: Missing docstring in public method
.\lab3\directory.py:64 in public method `display_all_records`:
        D102: Missing docstring in public method
.\lab3\__init__.py:1 at module level:
        D104: Missing docstring in public package
.\tests\__init__.py:1 at module level:
        D104: Missing docstring in public package
```
### pydocstyle results after first fixes.
```
.\tests\test_find_number.py:4 in public class `TestFindNumberCases`:
        D101: Missing docstring in public class
.\tests\test_find_number.py:6 in public method `test_find_number`:
        D102: Missing docstring in public method
.\tests\test_find_words.py:4 in public class `TestFindWordsCases`:
        D101: Missing docstring in public class
.\tests\test_find_words.py:6 in public method `test_find_words`:
        D102: Missing docstring in public method
```
### No more pydocstyle warnings at the end :).

## Prospector.
### Initial results.
```
Messages
========

lab1\find_number.py
  Line: 25
    pylint: no-else-break / Unnecessary "elif" after "break" (col 8)
  Line: 26
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 18)
  Line: 29
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 18)
  Line: 31
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 18)

lab3\directory.py
  Line: 42
    pylint: redefined-builtin / Redefining built-in 'id' (col 28)



Check Information
=================
         Started: 2021-04-12 18:41:23.308252
        Finished: 2021-04-12 18:41:24.900165
      Time Taken: 1.59 seconds
       Formatter: grouped
        Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
      Strictness: None
  Libraries Used:
       Tools Run: dodgy, mccabe, pep8, profile-validator, pyflakes, pylint
  Messages Found: 5
```