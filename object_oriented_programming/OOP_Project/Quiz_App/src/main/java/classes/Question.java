package classes;

import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;

import java.util.ArrayList;
import java.util.Objects;

/** Class Name: Question

 * Attributes: Category, Type[MCQ], Difficulty[Medium], question: is the question title,
 * correct_answer, answers[], givePoint

 * Methods:
 * +Question()
 * +Question(question_title, correct_answer, answers[])
 * +getQuestion(), +getCorrect_answer(), +getAnswers()
 * +render(label, radio_buttons)
 * +checkAnswer(selected_radio_answer)
 */
public class Question {
        protected String category;
        protected String type = "MCQ";
        protected String difficulty = "Medium";
        protected String question;
        protected String correct_answer;
        protected String[] answers;
        boolean givePoint;


        public Question() { // default
        }

        public Question(String question, String correct_answer, String[] answers) {
            this.answers = answers;
            this.correct_answer = correct_answer;
            this.question = question;
        }



    public String getQuestion() {
        return question;
    }

    public String[] getAnswers() {
        return answers;
    }

    public String getCorrect_answer() {
        return correct_answer;
    }

    // To Set The Question Title
    public void render(Label l, ArrayList<RadioButton> arr) {
        l.setText(this.question);
        for(int i = 0; i < 4; i++) {
            arr.get(i).setText(this.answers[i]);
        }
    }

    // To Check The User Answer
    public boolean checkAnswer(String answer) {
        return this.givePoint = (Objects.equals(this.correct_answer, answer));
    }

}