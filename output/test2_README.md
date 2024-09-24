# Simple Calculator Script

This script contains a simple calculator for addition and multiplication of two numbers.

## Table of Contents

- [Functions](#functions)
  - [add(a, b)](#addab)
  - [multiply(a, b)](#multiplyab)
- [Main Execution](#main-execution)

## Functions

### add(a, b)

This function takes two numbers as arguments and returns their sum.

#### Example

```javascript
add(5, 3); // Returns: 8
```

### multiply(a, b)

This function takes two numbers as arguments and returns their product.

#### Example

```javascript
multiply(5, 3); // Returns: 15
```

## Main Execution

The script calculates the sum and product of two numbers, `num1` and `num2`, and logs the results to the console.

```javascript
const num1 = 10;
const num2 = 5;

console.log(`The sum of ${num1} and ${num2} is:`, add(num1, num2));
console.log(`The product of ${num1} and ${num2} is:`, multiply(num1, num2));
```

#### Output

```
The sum of 10 and 5 is: 15
The product of 10 and 5 is: 50
```