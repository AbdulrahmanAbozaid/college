# Face Recognition Attendance System

The Face Recognition Attendance System is a computer vision-based application that records and manages attendance using facial recognition. It allows users to upload images or folders of images to detect faces, and records the attendance data in a CSV file. Users can also view attendance records for specific dates.

## Features

- **Facial Recognition**: Detects faces in images and records attendance.
- **CSV Export**: Exports attendance data to a CSV file.
- **View Attendance**: View attendance data for any specific date.
- **User-Friendly GUI**: Provides an easy-to-use graphical interface.

## Requirements

- Python 3.6 or higher
- Required Python packages (can be installed via `requirements.txt`):
  - face_recognition
  - tkinter
  - csv

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/face-recognition-attendance-system.git
    cd face-recognition-attendance-system
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **User Interface**:
    - **Choose Image**: Click the "Choose Image" button to select an image file. The application will detect faces and record attendance.
    - **Choose Folder**: Click the "Choose Folder" button to select a folder containing images. The application will detect faces in all images and record attendance.
    - **Enter Date**: Input a date in the format `YYYY-MM-DD` and click "Load Attendance" to view the attendance records for that specific date in a new window.

3. **Data Storage**:
    - Attendance data is stored in a CSV file named with the current date (e.g., `2023-05-27.csv`).
    - The CSV files are saved in the same directory as the script.

## Project Structure

- `main.py`: The main script to run the application.
- `models/`:
  - `datastore.py`: Handles data storage and retrieval.
  - `encoder.py`: Handles facial encoding and storage.
  - `utils.py`: Utility functions for the application.
- `README.md`: This file.
- `requirements.txt`: Lists required Python packages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
