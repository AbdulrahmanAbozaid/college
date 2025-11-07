package com.example.quiz_app;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class EndScene implements Initializable {
    @FXML
    private Button close;

    @FXML
    private Label result;
    @FXML
    private Label result2;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Closing Action Button
        close.setOnAction(e -> {
            Stage stg = (Stage) ((Node) e.getSource()).getScene().getWindow();
            stg.close();
        });
    }

    // Displaying The Number Of Correct Answers To The User
    public void setResult(String res, String res2) {
        result.setText(res);
        result2.setText(res2);
    }
}
