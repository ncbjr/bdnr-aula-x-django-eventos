# Start from Python 3.7
FROM django:base

# Copy the project code
WORKDIR /usr/src/app
COPY ./ /usr/src/app/

# Container listens on port 8000
EXPOSE 80

# Running the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]