package Module3;

import java.util.ArrayList;
import java.util.Scanner;

public class TodoListManager {
    private ArrayList<String> todoList;

    public TodoListManager() {
        todoList = new ArrayList<>();
    }

    public void addTask(String task) {
        todoList.add(task);
        System.out.println("Task added: " + task);
    }

    public void removeTask(int index) {
        if (index >= 0 && index < todoList.size()) {
            String removedTask = todoList.remove(index);
            System.out.println("Task removed: " + removedTask);
        } else {
            System.out.println("Invalid index!");
        }
    }

    public void displayTasks() {
        if (todoList.isEmpty()) {
            System.out.println("Todo list is empty");
        } else {
            System.out.println("Todo List:");
            for (int i = 0; i < todoList.size(); i++) {
                System.out.println((i + 1) + ". " + todoList.get(i));
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TodoListManager todoListManager = new TodoListManager();

        boolean quit = false;
        while (!quit) {
            System.out.println("\nTodo List Manager\n");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. Display Tasks");
            System.out.println("4. Quit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            switch (choice) {
                case 1:
                    System.out.print("Enter task to add: ");
                    String taskToAdd = scanner.nextLine();
                    todoListManager.addTask(taskToAdd);
                    break;
                case 2:
                    System.out.print("Enter index of task to remove: ");
                    int taskIndexToRemove = scanner.nextInt();
                    todoListManager.removeTask(taskIndexToRemove - 1);
                    break;
                case 3:
                    todoListManager.displayTasks();
                    break;
                case 4:
                    quit = true;
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 4.");
            }
        }

        scanner.close();
    }
}
