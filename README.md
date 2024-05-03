# data-fetch

# Data Fetch API

This project is a Django-based REST API designed to fetch data from a CSV file and expose it through an API endpoint. Below are the steps to set up and run the project on a new system.

## Prerequisites

- Python (3.6 or higher)
- Django (3.x)
- Django REST Framework

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/your-repository/data-fetch.git
   cd data-fetch
   ```

2. **Set up a Virtual Environment (Recommended)**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the Database**
   - This project uses SQLite by default. If you want to use another database, configure it in the `settings.py` file.
   ```
   python manage.py migrate
   ```

5. **Load Data into the Database**
   - Ensure your CSV file is formatted correctly and located at a path accessible to the Django app.
   - Use the following command to load data from the CSV into the database:
   ```
   python manage.py savecsv
   ```

6. **Run the Development Server**
   ```
   python manage.py runserver
   ```

7. **Access the API**
   - The API can be accessed at `http://localhost:8000/<bank_branch>` where `<bank_branch>` is the branch code for which you want to fetch details.

## Additional Information

- **API Endpoints**: This application contains a single endpoint that allows users to retrieve bank details by branch code.
- **Security**: Ensure you configure proper security settings before deploying the application in a production environment.

## Troubleshooting

- If you encounter issues with database migrations, make sure your database user has the appropriate permissions and that your database settings are correctly configured in `settings.py`.
- For issues related to dependency installations, ensure that your virtual environment is activated and that you have the necessary permissions to install packages.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
