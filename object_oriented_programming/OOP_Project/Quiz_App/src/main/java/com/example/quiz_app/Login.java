package com.example.quiz_app;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.ResourceBundle;

// *** Login Page Controller ***
// * To Get Username And Determine if he is a Doctor or Student


public class Login implements Initializable {

    @FXML
    private RadioButton instructor;
    @FXML
    private Button login;
    @FXML
    private TextField name;
    @FXML
    private RadioButton student;
    public String username;
    public String role;

    // When Starting login Page
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        ArrayList<RadioButton> rb = new ArrayList<>(2);
        rb.addAll(Arrays.asList(student, instructor));

        // Disabling login Button until setting Name and Role
        login.setDisable(true);

        this.name.setOnKeyTyped(e -> {
            if(student.isSelected() || instructor.isSelected()) {
                setData();
            }
        });

        rb.forEach(radioButton -> radioButton.setOnAction(e -> {
            if(!this.name.getText().isBlank()) {
                setData();
            }
        }));
    }

    // Getting Typed Data And Assigning them to Attributes
    private void setData() {
        this.username = this.name.getText();
        this.role = (student.isSelected()) ? "Student" : "Teacher";
        login.setDisable(false);
    }

    @FXML
    public void login(ActionEvent e) {
        if(!this.name.getText().isEmpty()) {
            try {
                // Switching Login Scene To Main Page Scene
                Stage stage = (Stage) ((javafx.scene.Node) e.getSource()).getScene().getWindow();
                FXMLLoader loader = new FXMLLoader(HelloApplication.class.getResource("mainPage.fxml"));
                Parent root = loader.load();
                Scene scene = new Scene(root);
                MainPage mp = loader.getController();
                mp.setUser(this.username, this.role);

                stage.setX(315);
                stage.setY(100);


                Image logo = new Image("idea.png");
                stage.getIcons().add(logo);
                stage.setTitle("Quiz App");
                stage.setScene(scene);
                setAlert(stage);
                stage.show();
            } catch (Exception err) {
                err.printStackTrace();
            }
        }
    }

    // Setting Logout Alert
    private void setAlert(Stage stg) {
        alerts(stg);
    }

    // To Use It at MainPage Too
    static void alerts(Stage stg) {
        stg.setOnCloseRequest(event -> {
            event.consume();
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
            alert.setTitle("Close Quiz App");
            alert.setHeaderText("are u sure to close?");
            alert.initOwner(stg);

            if(alert.showAndWait().get() == ButtonType.OK) {
                stg.close();
            }
        });
    }
}
