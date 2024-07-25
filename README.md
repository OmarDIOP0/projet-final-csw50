# Course Master

Course Master is a web application developed with Django for the backend and React for the frontend. The application allows users to register, log in, log out, view a dashboard, browse courses, take lessons, pass quizzes, and receive a completion certificate in PDF format.

### Distinctiveness and Complexity

Course Master stands out due to its seamless integration of Django and React, providing an interactive and responsive user experience. Key features include:

- **User Management System**: User registration, login, and logout.
- **User Dashboard**: View for each user with a list of available courses.
- **Course Navigation**: Viewing videos and PDF files for each lesson.
- **Quiz System**: Quizzes for each lesson, required to progress to the next lesson.
- **Completion Certificate**: Dynamic PDF generation of certificates after completing all quizzes in a course.

These features demonstrate technical complexity, especially in integrating React with Django, managing user states, and dynamically generating PDFs.

## Project Structure

### Backend (Django)

- `manage.py`: Main management script for the Django project.
- `coursemaster/`: Main Django project directory.
  - `settings.py`: Project configuration.
  - `urls.py`: Main project routing.
  - `wsgi.py`: WSGI entry point for deployment.
- `courses/`: Django app managing courses.
  - `models.py`: Data models for users,profile,courses,lessons and quiz.
  - `views.py`: Views for the user interface.
  - `urls.py`: Routing specific to the courses app.
  - `serializers.py`: Data serialization for APIs.
  - `admin.py`: Admin interface configuration.
- `media/lessons/files`:contained PDF files 

### Frontend (React)
- `src/`: Main React frontend directory.
  - `App.js`: Main application component.
  - `index.js`: Frontend entry point.
  - `components/`: React components used in the application.
    - `Breadcrumbs.js`:Component for helping users to keep track of their locations.
    - `CertificateDocument.js`: component that allows you to manage certificate generation.
    - `CourseDetail.js`: Component for displaying course details.
    - `Navbar.js`: Component to manage navigation
    - `NavbarWrapper.js`: Component for displaying the Navbar only if the user is registering.
    - `QuizList.js`: Component for displaying quizzes.
    - `SearchResults.js`: Component for managing search results.
    - `Welcome.js`: Component for displaying welcome pages.
  - `context/`: Manage system context 
    - `AuthContext.js`: Component to manage the contexts of authentication,login, token and logout
  - `hooks/`: Custom hooks for managing state and effects.
    - `useCourse.js`: Hook for fetching course.
    - `useCourseDetails.js`: Hook for fetching course details.
    - `useQuiz.js`: Hook for fetching quiz.
  - `pages/`: Manage all pages.
    - `Dashboard.jsx`: Component for displaying dashboard screen.
    - `Home.jsx`: Component for displaying home screen.
    - `Login.jsx`: Component for displaying login screen.
    - `Register.jsx`: Component for displaying register screen.
  - `utils/`: Manage all pages.
    - `ProtectedRoute.jsx`: Component for protecting route.
    - `url.jsx`: Component for managing backend url.
    - `useAxios.jsx`: Component for managing token.

## Installation and Running

### Prerequisites

- Python 3.10.4
- Node.js and npm

### Installation

1. Install Python dependencies:

   pip install -r requirements.txt

3. Install JavaScript dependencies:

   npm install

### Running the Application

1. Start the Django server:

   cd backend
   python manage.py runserver

2. Start the React development server:

   cd frontend
   npm start

3. Access the application at [http://localhost:3000](http://localhost:3000).

## Additional Information

- **Database**: Course Master uses SQLite by default but can be configured to use other databases like PostgreSQL or MySQL.
- **Authentication**: User authentication is managed via JWT tokens.
- **API**: Course Master exposes RESTful APIs for interacting with course and user data.

## Python Packages

If you have added any Python packages that need to be installed to run your web application, make sure to add them to the `requirements.txt` file.
