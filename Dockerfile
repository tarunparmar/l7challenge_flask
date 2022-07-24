# init a base image (Alpine is small Linux distro)
FROM python:3.8
# install tk
RUN apt-get install -y python3-tk
# define the present working directory
WORKDIR /l7challenge_flask
# copy the contents into the working dir
ADD . /l7challenge_flask
# run pip to install the dependencies of the flask app
RUN python3 -m pip install -r requirements.txt
# update pip to minimize dependency errors 
RUN pip install --upgrade pip
# define the command to start the container
CMD ["python","run.py"]