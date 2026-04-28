For `robots.csv` and similar files:

* `battery_level` must be an integer between 0 and 100.
* `max_load` must be a non-negative floating point number.
* `zone` must be a non-empty string consisting of only upper case alphabetical characters.

For `destinations.csv` and similar files:

* `zone` must be a non-empty string consisting of only upper case alphabetical characters.

For `packages.csv` and similar files:

* `weight` must be a non-negative floating point number.

For `tasks.csv` and similar files:

* `source_id` must exist in the destination data,
* `target_id` must exist in the destination data,
* `package_id` must exist in the package data,
* `status` must be one of `pending` or `complete`.

rebort
['robot_id', 		'battery_level', 'max_load', 	'zone']

destinations
['destination_id', 							'zone']

packages
['package_id', 	'weight']

tasks
['task_id', 		'source_id', 		'target_id', 		'package_id', 		'status']



## Python 正则表达式常用符号三列表

## Python Regex Common Symbols in 3 Columns

| 符号                                                 | Python 例子                                  | 常见用途                              |
| ---------------------------------------------------- | -------------------------------------------- | ------------------------------------- |
| `.`                                                | `re.search(r"c.t", "cat")`                 | 匹配任意单个字符，如 `cat`、`cut` |
| `\d`                                               | `re.search(r"\d", "a1b")`                  | 匹配一个数字                          |
| `\D`                                               | `re.search(r"\D", "123a")`                 | 匹配一个非数字字符                    |
| `\w`                                               | `re.search(r"\w", "@a#")`                  | 匹配字母、数字、下划线                |
| `\W`                                               | `re.search(r"\W", "abc@")`                 | 匹配非字母数字下划线字符              |
| `\s`                                               | `re.search(r"\s", "a b")`                  | 匹配空格、Tab、换行等空白字符         |
| `\S`                                               | `re.search(r"\S", "   a")`                 | 匹配非空白字符                        |
| `*`                                                | `re.search(r"ab*", "abbb")`                | 前一个内容出现 0 次或多次             |
| `+`                                                | `re.search(r"ab+", "abbb")`                | 前一个内容出现 1 次或多次             |
| `?`                                                | `re.search(r"colou?r", "color")`           | 前一个内容出现 0 次或 1 次            |
| `{n}`                                              | `re.search(r"\d{4}", "2026")`              | 前一个内容恰好出现 n 次               |
| `{m,n}`                                            | `re.search(r"\d{2,4}", "123")`             | 前一个内容出现 m 到 n 次              |
| `[]`                                               | `re.search(r"[abc]", "dog and cat")`       | 从括号中选一个字符匹配                |
| `[^ ]`                                             | `re.search(r"[^0-9]", "123a")`             | 匹配“不在集合中”的字符              |
| `[a-z]`                                            | `re.search(r"[a-z]", "A1b")`               | 匹配某个范围内的字符                  |
| `^`                                                | `re.search(r"^abc", "abcdef")`             | 匹配字符串开头                        |
| `$`             | `re.search(r"abc$", "123abc")` | 匹配字符串结尾                               |                                       |
| `^...$`                                            | `re.fullmatch(r"\d+", "12345")`            | 限制整个字符串都符合某模式            |
| `()`                                               | `re.search(r"(\d{4})-(\d{2})", "2026-04")` | 分组并提取部分内容                    |
| `(?:...)`                                          | `re.search(r"(?:ab)+", "abab")`            | 只分组，不单独保存结果                |
| `\|`                                                | `re.search(r"cat\|dog", "dog")`             | 表示“或”                            |
| `\\`                                               | `re.search(r"\.", "a.b")`                  | 转义特殊字符，匹配真正的符号          |
| `\b`                                               | `re.search(r"\bcat\b", "a cat is here")`   | 匹配完整单词边界                      |
| `\B`                                               | `re.search(r"\Bcat\B", "scatters")`        | 匹配非单词边界                        |
| `(?P<name>...)`                                    | `re.search(r"(?P<year>\d{4})", "2026")`    | 命名分组，方便按名字取值              |
| `(?i)`                                             | `re.search(r"(?i)python", "PYTHON")`       | 忽略大小写匹配                        |
| `(?m)`                                             | `re.findall(r"(?m)^\d+", "123\nabc\n456")` | 多行模式下匹配每行开头/结尾           |
| `(?s)`                                             | `re.search(r"(?s)a.*b", "a\nxx\nb")`       |                                       |
