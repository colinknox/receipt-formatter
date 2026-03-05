from main import *

run_cases = [
    (
        "Burger: $5.00\nFries: $2.00",
        "=== RECEIPT ===\nBurger: $5.00\nFries: $2.00\nTax: $0.00\n=== THANK YOU ===",
    ),
]

submit_cases = run_cases + [
    (
        "Coffee: $3.50",
        "=== RECEIPT ===\nCoffee: $3.50\nTax: $0.00\n=== THANK YOU ===",
    ),
    (
        "Pizza: $12.00\nSoda: $1.50\nDessert: $4.00",
        "=== RECEIPT ===\nPizza: $12.00\nSoda: $1.50\nDessert: $4.00\nTax: $0.00\n=== THANK YOU ===",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n{input1}\n")
    print(f"Expected:\n{expected_output}\n")
    result = format_receipt(input1)
    print(f"Actual:\n{result}\n")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()