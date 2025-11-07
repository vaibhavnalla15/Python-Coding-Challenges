**Mistakes in Challenge 1 (Temperature Converter):**

1. **Compared variable to variable instead of string literals**

   * You used `if unit_type == F:` instead of `if unit_type == "F":`.

2. **Used two independent `if` statements**

   * Caused `else` to attach only to the second `if`, skipping invalid input logic.

3. **Formulas reversed**

   * You swapped Celsius-to-Fahrenheit and Fahrenheit-to-Celsius conversions.

4. **Unnecessary variable initialization**

   * Declared `F = 0`, `C = 0` without purpose.

5. **Unclear variable naming**

   * Used `F` or `C` to store the converted temperature, which can confuse readers.

6. **Output not labeled with unit**

   * Printed only the numeric value, not `"°C"` or `"°F"` for clarity.

