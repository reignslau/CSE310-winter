#include <iostream>

using namespace std;

int main() {
    // Declare variables to store input numbers and sum
    int num1, num2, sum;

    // Prompt user to enter the first number
    cout << "Enter the first number: ";
    cin >> num1;

    // Prompt user to enter the second number
    cout << "Enter the second number: ";
    cin >> num2;

    // Calculate the sum
    sum = num1 + num2;

    // Display the sum
    cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << endl;

    return 0;
}
