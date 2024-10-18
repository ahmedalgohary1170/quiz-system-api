# Quiz System API - Django REST Framework

This is a quiz management system built using Django and Django REST Framework. The project supports multiple user roles (Teachers and Students) and uses JWT authentication for secure access to the API.

## Features

- **Teacher Role**: 
  - Create and manage quizzes with multiple-choice questions.
  - Assign quizzes to students.
  - View students' submissions and scores.
  
- **Student Role**:
  - View and take quizzes assigned to them.
  - Submit answers for grading.
  - View scores after submission.

- **Authentication**: 
  - Uses JWT (JSON Web Tokens) for authentication.
  - Role-based access control to ensure proper permissions (teachers can create quizzes, students can only take them).
  
- **Automatic Grading**:
  - The system automatically grades quizzes based on correct answers.

## Requirements

- Django==5.1.2
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- PyJWT==2.9.0
- sqlparse==0.5.1



