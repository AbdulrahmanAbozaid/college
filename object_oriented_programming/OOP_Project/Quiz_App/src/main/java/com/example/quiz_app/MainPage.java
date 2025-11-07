package com.example.quiz_app;

import classes.quizController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

import java.net.URL;
import java.util.Objects;
import java.util.ResourceBundle;


public class MainPage implements Initializable {

    @FXML
    private Label username;
    @FXML
    private Label userRole;
    @FXML
    private Pane user;
    @FXML
    private HBox userData;
    @FXML
    private Button createButton;

    // Start First Quiz Button
    @FXML
    public void startQuiz() {
        try {
            FXMLLoader loader = new FXMLLoader(Objects.requireNonNull(getClass().getResource("home.fxml")));
            quizController qct = new quizController(1);
            setController(loader, qct);

        } catch (Exception err) {
            //System.out.println(err);
            err.printStackTrace();
        }
    }


    // Setting Stage To manage the chosen Quiz
    private void setController(FXMLLoader loader, quizController qct) throws java.io.IOException {
        loader.setController(qct);
        Parent root = loader.load();
        Stage stage = new Stage();
        Scene scene = new Scene(root);

        Image logo = new Image("idea.png");
        stage.getIcons().add(logo);
        stage.setTitle("Quiz");
        stage.setScene(scene);
        stage.show();
    }


    // Start Second Quiz Button
    @FXML
    public void startQuiz2() {
        try {
            FXMLLoader loader = new FXMLLoader(Objects.requireNonNull(getClass().getResource("home.fxml")));
            quizController qc = new quizController(2);
            setController(loader, qc);
        } catch (Exception err) {
            err.printStackTrace();
        }
    }


    // Close quiz App Action Button Alert
    @FXML
    public void closeQuizApp(ActionEvent e) {
        Stage stg = (Stage) ((javafx.scene.Node) e.getSource()).getScene().getWindow();
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Close Quiz App");
        alert.setHeaderText("are u sure to close?");
        alert.setContentText("press enter or click ok");
        alert.initOwner(stg);
        if(alert.showAndWait().get() == ButtonType.OK) {
            stg.close();
        }
    }
    private boolean toggle = true;

    // Toggling User Data
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        userData.setVisible(false);

        user.addEventHandler(MouseEvent.MOUSE_CLICKED, e -> {
            e.consume();
            userData.setVisible(toggle);
            toggle = !toggle;
        });
    }

    // Determine User and Prevent Student From Add New Quiz
    public void setUser(String name, String role) {
        this.username.setText(name);
        this.userRole.setText(role);
        if(Objects.equals(role, "Student")) this.createButton.setVisible(false);
    }
}
