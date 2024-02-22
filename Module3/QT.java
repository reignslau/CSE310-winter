import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Question {
    private String question;
    private List<String> options;
    private int correctOption;

    public Question(String question, List<String> options, int correctOption) {
        this.question = question;
        this.options = options;
        this.correctOption = correctOption;
    }

    public String getQuestion() {
        return question;
    }

    public List<String> getOptions() {
        return options;
    }

    public int getCorrectOption() {
        return correctOption;
    }
}

public class QuizGame {
    private List<Question> questions;
    private int score;

    public QuizGame() {
        questions = new ArrayList<>();
        score = 0;
        initializeQuestions();
    }

    private void initializeQuestions() {
        // Add your questions here
        List<String> options1 = Arrays.asList("A. Option A", "B. Option B", "C. Option C", "D. Option D");
        questions.add(new Question("Question 1?", options1, 1));

        List<String> options2 = Arrays.asList("A. Option A", "B. Option B", "C. Option C", "D. Option D");
        questions.add(new Question("Question 2?", options2, 2));

        // Add more questions...
    }

    public void startGame() {
        Scanner scanner = new Scanner(System.in);
        for (Question q : questions) {
            System.out.println(q.getQuestion());
            List<String> options = q.getOptions();
            for (String option : options) {
                System.out.println(option);
            }
            System.out.print("Enter your choice (A, B, C, or D): ");
            String userChoice = scanner.nextLine().toUpperCase();
            int userOption = userChoice.charAt(0) - 'A';
            if (userOption == q.getCorrectOption()) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Incorrect!");
            }
            System.out.println();
        }
        scanner.close();
        System.out.println("Quiz completed! Your score is: " + score + "/" + questions.size());
    }

    public static void main(String[] args) {
        QuizGame quizGame = new QuizGame();
        quizGame.startGame();
    }
}
