package com.example.quiz_app;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

/**
 * Class Name: Final : To Handle Ending A Quiz Action And Display The Results
 * Attributes: correctAnswers, timeRecord
 * Methods:
 * +++Final()
 * +++getEndScene(btn): to switch Quiz Scene To Final Scene
 * */

public class Final {
    private final String correctAnswers;
    private final String timeRecord;


    public Final(String res, String res2) {
        this.correctAnswers = res;
        this.timeRecord = res2;
    }

    public void getEndScene(Button b) {
        try {
            // Loading Final Scene
            FXMLLoader loader = new FXMLLoader(getClass().getResource("endScene.fxml"));
            Parent root = loader.load();
            EndScene end = loader.getController();
            end.setResult(this.correctAnswers, this.timeRecord);


            Stage stg = (Stage) b.getScene().getWindow();
            Scene sc = new Scene(root);
            stg.setY(250);
            stg.setX(490);
            stg.setScene(sc);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
