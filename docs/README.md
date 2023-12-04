# flask_e2e_project
## HHA 504 Final Assignment/Project

**This file contains all of my documentation and references all of my screenshots and videos.**

## **Web Service Created**
The web service created is a comprehensive platform dedicated to women's health, developed using Flask, Python, HTML, and CSS. It features a user-friendly navigation bar with tabs for various sections, including Home, About, Reproductive Health, Mental Well-Being, Fitness, Data, and Contact.

The "Home" and "About" tab explain the purpose for this platform and how it can help women's health. It also can be used as a learning platform to discover new resources. The "Reproductive Health," "Mental Well-Being," and "Fitness" tabs summarize important aspects of women's health.  

Each tab leads to specific content pages offering valuable information related to the respective health category. Notably, the "Data" tab dynamically loads information from a CSV file and other datasets, allowing users to explore various datasets related to women's health.

The "Contact" tab includes a form for users to submit their name, email, and a message. After submission, users are redirected to a "Thank You" page. The web service utilizes CSS, with a mention of Tailwind CSS for frontend styling.

The deployment is intended for Google Cloud Shell, emphasizing a cloud-based hosting solution. Overall, the web service provides a rich and interactive experience for users seeking information and resources on women's health.

## **Technologies Used**

For this Women's Health App, I used various technologies. 

**Version Control:**
GitHub

**Web Framework:**
Flask (Python) for both Frontend and Backend development.

**Database Management System:**
MySQL, with the option to choose between Google Cloud Platform (GCP) or Azure for cloud-based deployments.

**Object-Relational Mapping (ORM):**
SQLAlchemy

**Environment Variables:**
.env for managing environment variables.

**Frontend Styling:**
Tailwind CSS for styling the frontend.

**Authorization:**
Google OAuth for user authentication and authorization.

**API Service:**
Flask used as the backend to provide API services.

**Debugging & Logging:**
Logger for logging and Sentry.io for error tracking and debugging.

**Containerization:**
Docker for containerizing the application.

**Cloud Deployment:**
Google Cloud Platform (GCP) or Azure for deploying the application to the cloud.

This technology stack indicates a modern web development setup, integrating various tools and services to cover version control, web framework, database management, security, logging, containerization, and cloud deployment. The choice of technologies reflects a well-rounded approach to building and deploying web applications with a focus on scalability, security, and maintainability.

## **Steps to Run the Web Service if Someone Wanted to Run Locally or Deploy to the Cloud**

## **Template of the .env File Structure**
DB_HOST=

DB_DATABASE=

DB_USERNAME=

DB_PASSWORD=

DB_NAME=

DB_PORT=

DB_CHARSET=
