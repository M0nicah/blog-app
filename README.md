# blog-app
An app for posting blogs, and updating them. It also contains inspirational quotes to inspire the readers.

## Installation

Guide to install Blogify application:

### Clone this repository
```bash
git clone https://github.com/M0nicah/blog-app.git
```
* Move into the cloned directory:
```bash
cd blog-app
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or

```bash
(Virtual)$ python3 manage.py
```
## Features and BDD

- Users are able to create user profile and login to post their .

## Technology Used

- **Framework:** Flask
- **Language** Python

### Developed with
- **Structure:** Bootstrap, HTML

- **Styles:** CSS

## Author

* Designed and developed by: [Monica Masae](https://github.com/M0nicah)
