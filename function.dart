// Task 1: Add Two Numbers
int addTwo(int num1, int num2) {
  return num1 + num2;
}

// Task 2: Subtract Two Numbers
int subtractTwo(int num1, int num2) {
  return num1 - num2;
}

// Task 3: Multiply Two Numbers
int multiplyTwo(int num1, int num2) {
  return num1 * num2;
}

// Task 4: Divide Two Numbers
double divideTwo(int num1, int num2) {
  if (num2 != 0) {
    return num1 / num2;
  } else {
    print("Error: Cannot divide by zero.");
    return double.nan; // Not a Number
  }
}

// Task 5: String Length
int stringLength(String text) {
  return text.length;
}

// Task 6: Get First Element of a List
dynamic getFirstElement(List<dynamic> list) {
  if (list.isNotEmpty) {
    return list[0];
  } else {
    print("Error: The list is empty.");
    return null;
  }
}

void main() {
  // Example usage:
  print("Task 1: ${addTwo(5, 3)}"); // Output: 8
  print("Task 2: ${subtractTwo(8, 3)}"); // Output: 5
  print("Task 3: ${multiplyTwo(2, 4)}"); // Output: 8
  print("Task 4: ${divideTwo(10, 2)}"); // Output: 5.0
  print("Task 5: ${stringLength("Dart is awesome!")"); // Output: 17
  print("Task 6: ${getFirstElement([1, 2, 3])}"); // Output: 1
}
