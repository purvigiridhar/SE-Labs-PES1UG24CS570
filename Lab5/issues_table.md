# Lab 5: Static Code Analysis Issue Document

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **B608: hardcoded_sql_expressions** | Bandit (Security) | 9 | SQL Injection vector through string-based query construction using `.format()` | Replaced string formatting with parameterized query `(?, ?, ?)` |
| **B324: hashlib (Weak Hash)** | Bandit (Security) | 15 | Use of weak `hashlib.md5` hash algorithm | Replaced `hashlib.md5` with `hashlib.sha256` |
| **B101: assert_used** | Bandit (Security) | 36 | Use of `assert` statement in production code | Replaced `assert` check with an explicit `if` statement raising a `ValueError` |
| **W0102: dangerous-default-value** | Pylint (Quality) | 8 | Dangerous default mutable argument `extras={}` shared across calls | Changed default argument to `None` and initialized `extras = {}` inside the function |
| **C0103: invalid-name / PEP 8** | Pylint / Flake8 (Style) | 8, 14, 18, 28 | Function names using camelCase (`logSighting`, `observerId`, `zoneSummary`) and single-letter variable `l` | Renamed functions to snake_case (`log_sighting`, `observer_id`, `zone_summary`) and renamed `l` to `least_sighted` |
| **E501 / C0301: Line too long** | Flake8 / Pylint (Formatting) | 5, 9, 19, 27 | Lines exceeded character limit (over 79/100 characters) | Split statements across multiple lines with proper indentations |
| **C0114 / C0116: Missing docstrings** | Pylint (Quality) | 1, 8, 14, 18, 26, 32 | Missing module and function docstrings | Added informative docstrings for the module and all functions |