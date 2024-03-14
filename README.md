# Web Application for Data Input and Display

This is a simple web application built with Python and Flask that allows users to input data, validate it, store it in a SQLite database, retrieve it, and display it in a table format.

## Prerequisites

- Python 3.x
- Flask
- SQLite3 (included in Python's standard library)

## Installation

1. Clone the repository or download the project files.

```
git clone https://github.com/your-username/web-app.git
```

2. Navigate to the project directory.

```
cd web-app
```

3. Create a virtual environment (optional but recommended).

```
python -m venv env
```

4. Activate the virtual environment.

```
# On Windows
env\Scripts\activate

# On Unix/Linux
source env/bin/activate
```

5. Install the required Python packages.

```
pip install flask
```

## Running the Application

1. Make sure you're in the project directory.

2. Run the Flask application.

```
python app.py
```

3. The application should now be running at `http://127.0.0.1:5000/` or `http://localhost:5000/`.

4. Open your web browser and navigate to `http://127.0.0.1:5000/` or `http://localhost:5000/`.

5. You should see the "Input Data" page.

6. Enter the required data (name, email, age, date of birth, and phone number) and click "Submit".

7. The data will be stored in the SQLite database (`data.db` file) located in the project directory.

8. To view the stored data, click the "View Data" link or navigate to `http://127.0.0.1:5000/data` or `http://localhost:5000/data`.

9. The data will be displayed in a table format.

10. To stop the Flask development server, go back to the terminal and press `Ctrl+C`.

## File Structure

```
web-app/
    app.py
    data.db
    templates/
        index.html
        data.html
    static/
        styles.css
```

- `app.py`: The Flask application code.
- `data.db`: The SQLite database file where the data is stored.
- `templates/`: Directory containing HTML templates for the web pages.
- `static/`: Directory for static files like CSS stylesheets.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

