package classes;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;

import java.net.URL;
import java.util.*;

/* ************************************** Quiz Page Controller ********************************************** */

public class quizController implements Initializable {
    @FXML
    public Label category;
    @FXML
    public Label count;
    @FXML
    public RadioButton ans1;
    @FXML
    public RadioButton ans2;
    @FXML
    public RadioButton ans3;
    @FXML
    public RadioButton ans4;
    @FXML
    public Button submit_btn;
    @FXML
    public Label timer;
    @FXML
    public Label question_title;
    public int currQuiz;


    // Constructor To Determine the Current Chose Quiz
    public quizController(int num) {
        this.currQuiz = num;
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        // To Store Choices Radio Buttons
        ArrayList<RadioButton> ar = new ArrayList<>(4);
        ar.addAll(Arrays.asList(ans2, ans1, ans4, ans3));

        // Instantiating Quiz from Quiz Class To Start Quiz.
        Quiz quiz = new Quiz(question_title, ar, this.count, this.submit_btn, this.timer, this.currQuiz, this.category);

        // Disabling Buttons Until Choosing Answer
        submit_btn.setDisable(true);
        // Activating Submit Button When Choosing any Answer (At First Question)
        ar.forEach(radioButton -> radioButton.setOnAction(e -> submit_btn.setDisable(false)));

        // Setting ActionHandler for Submit Button To Get The Next Question
        submit_btn.setOnAction(e -> {
            quiz.nextQuestion((Button)e.getSource());

            // After Getting Next Question One Radio Button Still Selected So We Remove that
            ar.forEach(radioButton -> {
                radioButton.setSelected(false);

                radioButton.setOnAction(r -> submit_btn.setDisable(false));
            });
            // Disabling Submit Button Until Choosing an Answer
            submit_btn.setDisable(true);
        });
    }
}
