#include <iostream>

// Function to calculate factorial recursively
unsigned long long factorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    std::cout << "Enter a non-negative integer to calculate its factorial: ";
    std::cin >> num;

    if (num < 0) {
        std::cout << "Factorial is not defined for negative numbers." << std::endl;
    } else {
        unsigned long long fact = factorial(num);
        std::cout << "Factorial of " << num << " is: " << fact << std::endl;
    }

    return 0;
}
