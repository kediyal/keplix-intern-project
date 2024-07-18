# Design a Car Inventory Management System

This project is part of the assignment for the Keplix Intern Role.

### Project Structure

1. The project is named `cars_inventory`, and this directory contains all the project-related files.
2. There is an additional directory `cars` which contains all the files handling the functionality related to managing cars on the website.
3. The `accounts` directory contains the logic for signup process with a custom signup form.
4. The directory `templates` contains all the styling and the webpages of the website.

### Functionalities
1. **User Authentication:** Password change, password reset, user registration, user login, user logout
2. **Car Management:** Add new car, view car details, update car details, delete car
3. **User Interface:** Responsive design with Bootstrap, navigation bar with authentication status, user-friendly forms with validation
4. **Admin Interface:** Access to Django admin panel, manage users and cars


### How to Run the Project

Follow these steps to set up and run the project locally:

#### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

#### Steps

1. **Clone the repository:**

    ```bash
    git clone git@github.com:kediyal/keplix-intern-project.git
    cd keplix-assignment
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
      ```bash
      .\.venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000` to view the application.

### Additional Notes

- To access the Django admin interface, navigate to `http://127.0.0.1:8000/admin` and log in with the superuser account you created.
- The `cars` directory handles all the core functionality related to the car inventory management.
- The `templates` directory contains the HTML templates used for rendering the web pages.

Feel free to explore the codebase and make any necessary modifications. If you encounter any issues or have questions, please refer to the Django documentation or reach out for support.

