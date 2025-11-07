package com.example.quiz_app;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) {
        try {
            FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("login.fxml"));
            Scene scene = new Scene(fxmlLoader.load());

            Image logo = new Image("idea.png");
            stage.getIcons().add(logo);
            stage.setTitle("Quiz App");
            stage.setScene(scene);
            setAlert(stage);
            stage.show();
        } catch (Exception e) {
                e.printStackTrace();
        }
    }

    private void setAlert(Stage stg) {
        Login.alerts(stg);
    }

    public static void main(String[] args) {
            launch(args);
    }
}