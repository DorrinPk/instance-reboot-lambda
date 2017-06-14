FROM amazonlinux

RUN mkdir -p ~/.aws

RUN yum -y update
RUN yum -y install gcc openssl-devel libffi-devel git epel-release
RUN yum -y install python27-pip python27-wheel python27-devel
RUN pip install --upgrade pip

RUN mkdir /app
COPY reboot.py /app/reboot.py
COPY key /app/key
WORKDIR app 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
