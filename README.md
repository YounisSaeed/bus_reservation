# bus_reservation
Bus Resevation tickets system
## Role 
### Manager
* ( create - edit - delete - update ) Trip
* search in booking invoices 
* activate booking
### Passanger
* Browse for trips
* booking trips
* Generating automatic number for invoice
## Setup
* make virtualenv and put lib in new virtualenv
* install all lib in requirements.txt ( $ pip install -r requirements.txt )
* $ cd path/env/scripts/activate
* $ python manage.py createsuperuser
* username : yourname
* email : example@example.com
* password and reconfirm password
* after this $ python manage.py runserver
* http://127.0.0.1:8000/admin
* login use your account admin
* make two groups ( manager - passanger ) in groups table
* but any user in manager group
#### enjoy discovering website
