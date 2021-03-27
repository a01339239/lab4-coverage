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
Check this [commit](https://github.com/a01339239/lab4-coverage/commit/8a4fed4d80b90385192a1c9ea277f91721c0d42c).
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
Check this [commit](https://github.com/a01339239/lab4-coverage/commit/b2d150c7d6feb949174d416868a8ef1da6e4964e).
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
Check this [commit](https://github.com/a01339239/lab4-coverage/commit/e88b8e4e8cbefc8f35ea5d6c205402dd7e9dd361) and this [commit](https://github.com/a01339239/lab4-coverage/commit/1eb67ce7c71b0578004138d709ca6d47fdcefedd).
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
