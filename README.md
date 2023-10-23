# Sisyphus

Sisyphus is a Django application with a PostgreSQL backend designed to digitize processes in small enterprises. With Docker Compose, you can easily run Sisyphus in a containerized environment to manage tasks, sales, receivables, and more.

## Key Features
* Task Management: Plan, assign, and track tasks for your employees. Keep everyone on the same page and ensure that projects are completed efficiently.
* Sales Registration: Register sales quickly and efficiently, ensuring that your business transactions are accurately recorded.
* Billing: Easily generate and send invoices to your customers based on completed tasks and sales transactions.
* Payables Management: Manage your payables, allowing manual insertion or utilizing the Microsoft Form Recognizer for automated data entry.

## Prerequisits
Before running Sisyphus with Docker Compose, make sure you have the following prerequisites:
* Docker and Docker Compose installed.

## Installing
1. Clone this repository to your local environment.
```
bash
git clone https://github.com/fpfiste/sisyphus.git
```
2. Navigate to the project directory.
```
bash
cd sisyphus
```
3. Create a .env file based on the provided .env.prod and configure the necessary environment variables.

4. Build and start the application using Docker Compose.
```
bash
docker-compose -f docker-compose.prod.yml up -d
```

## Usage
1. Access the web application at http://localhost:1337 and begin using Sisyphus.
* Initial user: root
* Initial password: test

2. Log in to the application with the following credentials.
* Initial user: root
* Initial password: test

3. Create a new superuser in the admin panel (http://localhost:1337/admin) and delete the root user.
4. Go to the settings page and insert the configurations 
5. Utilize the various modules in Sisyphus to plan tasks, manage sales, handle payables, and generate invoices.
6. Explore the user-friendly interface to streamline your enterprise's business processes.
   
## Authors

Fabian Pfister  

## Version History


## Acknowledgments
* Special thanks to the Django and PostgreSQL communities for their invaluable contributions to this project.
