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