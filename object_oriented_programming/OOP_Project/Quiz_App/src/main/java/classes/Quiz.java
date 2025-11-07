package classes;

import com.example.quiz_app.Final;
import javafx.application.Platform;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;

import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;


/**
 * Class Name : Quiz : this is to Manage in-quiz actions like getting next question or get end page and so on.\

 * Attributes:
 * +++questionsHolder: this is To use Questions Class Here to get Questions From it [Association]
 * ---correctAnswers: to hold the correct answers from the quiz
 * ---currentQuestion, choicesRadioButtons, questionTitle, questionCount, submitBtn, countDownTimerLabel, quizDuration, countDownTimer
 * Methods:
 * +++Quiz(questionTitleLabel, radioButtonArrayList, countLabel, countDownTimer, currentQuiz[1 || 2], )
 * +++nextQuestion()
 * +++endQuiz()
 * +++setCount()
 * +++setQuizCategory()
 * ---setQuizTimer()
 * ---formatDuration()
 * ---setTime()
 * */

public class Quiz {

    public Questions questionsHolder;
    protected int correctAnswers = 0;
    protected int currentQuestion = 0;
    public ArrayList<RadioButton> choicesRadioButtons;
    public Label questionTitle;
    public Label questionCount;
    public Button submitBtn;
    public Label countDownTimerLabel;

    private int quizDuration = 60*7;
    private Timer countDownTimer;


    public Quiz(Label label, ArrayList<RadioButton> radioButtonArrayList, Label count, Button btn, Label countDownTimer, int currentQuiz, Label category) {

        // determine quiz
        this.questionsHolder = new Questions(currentQuiz);

        // setting category
        String quizCategory = currentQuiz==2 ? "Category: Science: Mathematics" : "Category: Science: Computers";
        category.setText(quizCategory);

        // setting data
        this.questionTitle = label;
        this.choicesRadioButtons = radioButtonArrayList;
        this.questionCount = count;
        this.submitBtn = btn;
        this.countDownTimerLabel = countDownTimer;



        // Displaying Questions to User And setting Timer
        this.renderQuestion(this.questionTitle, this.choicesRadioButtons);
        this.setCount(count);
        // @arg submitBtn  To get The Stage of The quiz and Switch it to Final Page When Time is up
        this.setQuizTimer(submitBtn);
    }


    /************************************************ Actions *****************************************/

    // when clicking submit btn | Submit
    public void nextQuestion(Button btn) {
        // Checking if the Current Choice is true or Not
        if(this.isTrue(this.choicesRadioButtons)) {
            correctAnswers++;
        }

        // Getting the next Question Index from @Object Questions
        currentQuestion++;
        if(this.currentQuestion < this.questionsHolder.getNumOfQuestions()) {
                this.setCount(this.questionCount);
                this.renderQuestion(this.questionTitle,this.choicesRadioButtons);
        } else  this.endQuiz(btn); // Finish After Submitting all Questions
    }

    // when finished | Finish
    public void endQuiz(Button btn) {
        String res = "Correct Answers: " + this.correctAnswers;
        String res2 = "Time: " + this.formatTimer(Math.abs(60*7 - this.quizDuration -1));

        // Association of Final Class To display Final Page
        Final fnl = new Final(res, res2);
        fnl.getEndScene(btn);
    }

    /*********************************************  Helper Methods( private )  ***********************************************/

    // Display The Number Of the Current Question From All Questions
    private void setCount(Label l) {
        l.setText((currentQuestion+1) +" / " + this.questionsHolder.getNumOfQuestions());
    }

    // get checked answer
    private String getAnswered(ArrayList<RadioButton> ar) {
        // Determine which answer is selected
        for(int i = 0; i < 4; i++) {
            if(ar.get(i).isSelected()) return ar.get(i).getText();
        }
        return "";
    }

    // check if the selected answer is true
    private boolean isTrue(ArrayList<RadioButton> al) {
        return  this.getCurrQuestion().checkAnswer(this.getAnswered(al));
    }

    // render next question
    private void renderQuestion(Label l, ArrayList<RadioButton> al) {
        this.getCurrQuestion().render(l, al);
    }

    // return current question of q ArrayList
    private Question getCurrQuestion() {
        return this.questionsHolder.getQuestions().get(currentQuestion);
    }


    /* ******************************************** COUNTDOWN Timer *****************************************/

    // Creating Timer
    private void setQuizTimer(Button button) {
        try {
            countDownTimer = new Timer();
            countDownTimer.scheduleAtFixedRate(this.getTask(button), 0, 1000);
        } catch (Exception e) {
            System.out.println("Error in setQuestionTimer: "+ e);
        }
    }

    private TimerTask getTask(Button button) {
            return new TimerTask() {
            @Override
            public void run() {
                Platform.runLater(() -> {
                    formatDuration(quizDuration);
                    quizDuration--;
                    if (quizDuration < 0 || currentQuestion >= questionsHolder.getNumOfQuestions()) {
                        countDownTimer.cancel();
                        if (button.getScene().getWindow() != null) endQuiz(button);
                    }
                });
            }
        };
    }

    // Format Timer To two Digits
    private void formatDuration(int s) {
        setTime(this.formatTimer(s));
    }
    private String formatTimer(int s) {
        int minutes;
        int seconds;

        if(s >= 60) {
            minutes = s / 60;
            seconds = s % 60;
        } else {
            minutes = 0;
            seconds = s;
        }


        String min = minutes <= 9 ? "0" + minutes : ""+minutes;
        String sec = seconds <= 9 ? "0" + seconds : ""+seconds;

        return (s > 0) ? (min + ":" + sec) : "00:00";
    }

    // Display Current Time of the Quiz
    private void setTime(String str) {
        this.countDownTimerLabel.setText(str);
    }

}
