FROM python

#This will create directory for commands of dockerfile
WORKDIR /myapp

#this will copy content from source directory  to destination directory.
COPY .  /myapp


RUN pip install -r requirements.txt


#Command which will be get excecuted ....
CMD [ "python3" , "manage.py" ,"runserver" , "0:8000" ]