#!/bin/bash
 # Activate your virtual environment (if using one)                                                                                                                                        
 source venv/bin/activate  # Replace 'venv' with your virtual environment name                                                                                                             
                                                                                                                                                                                           
 # Run migrations                                                                                                                                                                          
 python manage.py makemigrations                                                                                                                                                           
 python manage.py migrate
                                                                                                                                                                                           
 # Collect static files (if you have any)                                                                                                                                                  
 python manage.py collectstatic --noinput

 # Run the development server
 python manage.py runserver 0.0.0.0:8000
                                                                                                                                                                                           
 # Keep the script running until manually stopped (Ctrl+C)                                                                                                                                 
 wait                 
