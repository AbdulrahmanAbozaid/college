package classes;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


/**
 * Class Name: Questions : this is to get quiz questions and their answers [as a database for render quiz]
 * there are two quizzes by default
 * Attributes: questions, questionTitles: to store question titles and the correct_answer, questionAnswers: to store every question answers
 * ----------: questionTitles2 and questionAnswers2 to store second default set quiz answers
 *
 * Methods:
 * +Questions(): a Constructor to set quizzes data and to determine which of current two quizzes to display
 * */

public class Questions {
    // To hold a Question Instances that have been filled with required data
    private final ArrayList<Question> questions;

    /* Available quizzes Section Data Setting */

    // @questionTitles ArrayList that hold Maps each of which have two keys: "question"(for question_title) and "correct_answer"
    private final ArrayList<Map<String, String>> questionTitles = new ArrayList<>(10);
    private final ArrayList<String[]> questionAnswers = new ArrayList<>(10);
    private final ArrayList<Map<String, String>> questionTitles2 = new ArrayList<>(5);
    private final ArrayList<String[]> questionAnswers2 = new ArrayList<>(5);

    public Questions(int num) {
        // We Have put two quizzes Data in these Methods and invoked them here [quizzes' questions have been set Manually]
        this.setQuestionTitles();
        this.setQuestionAnswers();

        // Determine which quiz to send its data
        if(num == 2) {
            questions = new ArrayList<>(5);
            for(int i = 0; i < 5; i++) {
                this.addQuestion(this.questionTitles2.get(i).get("question"), this.questionTitles2.get(i)
                        .get("correct_answer"), this.questionAnswers2.get(i));
            }
        } else {
            questions = new ArrayList<>(10);
            for(int i = 0; i < 10; i++) {
                this.addQuestion(this.questionTitles.get(i).get("question"), this.questionTitles.get(i)
                        .get("correct_answer"), this.questionAnswers.get(i));
            }
        }
    }


    /* *************************************  Methods *********************************** */

    public ArrayList<Question> getQuestions() {
        return this.questions;
    }

    private void addQuestion(String question, String correct_answer, String[] answers) {
        Question q = new Question(question, correct_answer, answers);
        this.questions.add(q);
    }
    public void addQuestion(ArrayList<Question> arrayList, String question, String correct_answer, String[] answers) {
        Question q = new Question(question, correct_answer, answers);
        arrayList.add(q);
    }

    public int getNumOfQuestions() {
        return this.questions.size();
    }


    /* ************************************* Helper Methods(used here only) *********************************** */

    private void setQuestionTitles() {
        this.questionTitles.add(this.getMap(
                "Which of the following languages is used as a scripting language in the Unity 3D game engine?",
                "C#"
        ));
        this.questionTitles.add(this.getMap(
                "What did the name of the Tor Anonymity Network originally stand for?",
                "The Onion Router"
        ));
        this.questionTitles.add(this.getMap(
                "What was the first commercially available computer processor?",
                "Intel 4004"
        ));
        this.questionTitles.add(this.getMap(
                "While Apple was formed in California, in which western state was Microsoft founded?",
                "New Mexico"
        ));
        this.questionTitles.add(this.getMap(
                "How many cores does the Intel i7-6950X have?",
                "10"
        ));

        this.questionTitles.add(this.getMap(
                "In CSS, which of these values CANNOT be used with the &quot;position&quot; property?",
                "center"
        ));
        this.questionTitles.add(this.getMap(
                "Which operating system was released first?",
                "Mac OS"
        ));
        this.questionTitles.add(this.getMap(
                ".at is the top-level domain for what country?",
                "Austria"
        ));
        this.questionTitles.add(this.getMap(
                "What is known as &quot;the brain&quot; of the Computer?",
                "Central Processing Unit"
        ));
        this.questionTitles.add(this.getMap(
                "What does the term GPU stand for?",
                "Graphics Processing Unit"
        ));

        /* *********************************** Quiz2 ***************************************** */
        this.questionTitles2.add(this.getMap(
                "In the hexadecimal system, what number comes after 9?",
                "The Letter A"
        ));
        this.questionTitles2.add(this.getMap(
                "How many zeros are there in a googol?",
                "100"
        ));
        this.questionTitles2.add(this.getMap(
                "What's the square root of 49?",
                "7"
        ));
        this.questionTitles2.add(this.getMap(
                "What is the alphanumeric representation of the imaginary number?",
                "i"
        ));
        this.questionTitles2.add(this.getMap(
                "How many sides does a heptagon have?",
                "7"
        ));
    }
    private void setQuestionAnswers() {
        this.questionAnswers.add(this.getArrayOf("C#", "Java", "C++", "Objective-C"));
        this.questionAnswers.add(this.getArrayOf("The Only Router","The Orange Router","The Ominous Router", "The Onion Router"));
        this.questionAnswers.add(this.getArrayOf("Intel 486SX", "TMS 1000", "AMD AM386", "Intel 4004"));
        this.questionAnswers.add(this.getArrayOf("New Mexico", "Washington", "Colorado", "Arizona"));
        this.questionAnswers.add(this.getArrayOf("10", "12", "8", "4"));

        this.questionAnswers.add(this.getArrayOf("static", "absolute", "relative", "center"));
        this.questionAnswers.add(this.getArrayOf("Mac OS", "Windows", "Linux", "OS/2"));
        this.questionAnswers.add(this.getArrayOf("Austria", "Argentina", "Australia", "Angola"));
        this.questionAnswers.add(this.getArrayOf("Motherboard", "Graphics Processing Unit", "Keyboard", "Central Processing Unit"));
        this.questionAnswers.add(this.getArrayOf("Gaming Processor Unit","Graphite Producing Unit","Graphical Proprietary Unit","Graphics Processing Unit"));

        /* ******************************** Quiz2 ***************************************** */

        this.questionAnswers2.add(this.getArrayOf("The Letter A", "10", "The Number 0", "16"));
        this.questionAnswers2.add(this.getArrayOf("10", "1,000", "1,000,000", "100"));
        this.questionAnswers2.add(this.getArrayOf("7", "4", "12", "9"));
        this.questionAnswers2.add(this.getArrayOf("i", "e", "n", "x"));
        this.questionAnswers2.add(this.getArrayOf("6", "8", "7", "5"));

    }

    private Map<String, String> getMap(String question, String correct_answer) {
        Map<String, String> map = new HashMap<>();
        map.put("question", question);
        map.put("correct_answer", correct_answer);
        return map;
    }

    private String[] getArrayOf(String a,String b,String c,String d) {
        return new String[]{a, b, c, d};
    }

}