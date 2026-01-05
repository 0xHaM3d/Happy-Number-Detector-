# Happy Number Detector 

This Python script determines whether a given positive integer is a Happy Number.

A **Happy Number** is defined by the following process:

 1. Starting with any positive integer, replace the number with the sum of the squares of its digits.

 2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.

 3. Those numbers for which this process ends in 1 are **happy** :).

## 🚀 Features
 - **Mathematical Digit Extraction:** Uses `divmod()` for efficient digit processing instead of slower string conversions.

 - **Cycle Detection:** Implements a Python `set` to track previously seen numbers and prevent infinite loops.

 - **Robust Input Handling:** Includes a `try-except` block to catch non-integer inputs.

 - **Self-Testing:** Features a built-in test suite to verify logic accuracy upon execution.


## 🛠️ How it Works
The core logic resides in the `check_happiness` function:
 1. It stores the current number in a `history` set.
 2. It strips digits from the right using $num \pmod{10}$ and squares them.
 3. If the number hits 1, it returns `True`.
 4. If the number enters a sequence it has visited before, it returns `False`.

## 💻 Usage
Simply run the script in your terminal:

```Bash
python happy_number.py
```

### Example Output:
```Plaintext
Verification successful: All internal tests passed.
Enter a positive integer: 19
The number 19 is a Happy Number! :)
```

## 🧪 Built-in Tests
The script automatically validates the following cases before prompting for user input:

 - **Happy:** 7, 44

 - **Unhappy:** 45, 69
