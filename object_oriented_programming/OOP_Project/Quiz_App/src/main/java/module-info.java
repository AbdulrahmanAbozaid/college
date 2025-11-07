module com.example.quiz_app {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.quiz_app to javafx.fxml;
    exports com.example.quiz_app;
    exports classes;
    opens classes to javafx.fxml;
}