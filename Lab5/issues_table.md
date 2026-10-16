# Identified and Fixed Issues

| Issue Code | Tool | Category | Line(s) | Description | Fix Applied |
|---|---|---|---|---|---|
| B608 | Bandit | Security | 9 | SQL injection vector using `.format()` query construction | Converted to parameterized SQL query (`?, ?, ?`) |
| B324 | Bandit | Security | 15 | Weak MD5 cryptographic hashing algorithm | Upgraded to `hashlib.sha256()` |
| B101 | Bandit | Security | 36 | `assert` statement used in runtime logic | Replaced with explicit `if` check raising `ValueError` |
| W0102 | Pylint | Logic Bug | 8 | Dangerous mutable default argument `extras={}` | Set default parameter to `None` and initialized `{}` inside function |
| C0103 / E741 | Pylint / Flake8 | Style | 8, 14, 18, 28 | Non-conforming camelCase function names and ambiguous variable `l` | Renamed functions to snake_case (`log_sighting`, etc.) and `l` to `least_sighted` |
| E501 / C0301 | Flake8 / Pylint | Formatting | 5, 9, 19, 27 | Lines exceeding character limit (>79/100 chars) | Split queries and parameters across multiple lines |
| C0114 / C0116 | Pylint | Quality | 1, 8, 14, 18, 26, 32 | Missing module and function-level docstrings | Added structured docstrings across all modules and functions |

---

# Analysis Results & Improvement Metrics

| Tool | Pre-Fix Findings | Post-Fix Status | Improvement Summary |
|---|---|---|---|
| Pylint | Score: 3.46/10 (17 warnings/errors) | Score: 10.00/10 | Resolved mutable default args, shadowing, missing docstrings, and naming style violations. |
| Bandit | 3 Vulnerabilities (High: 1, Med: 1, Low: 1) | 0 Issues Identified | Replaced `MD5` with `SHA-256`, applied parameterized SQL queries, and removed `assert`. |
| Flake8 | 6 Style Violations | 0 Issues (Empty Report) | Resolved line length limits (E501), ambiguous variable names (E741), and formatting. |
