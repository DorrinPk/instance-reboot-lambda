# Script to reboot mnsockd servers as needed 
#!/usr/bin/env python

from __future__ import print_function

import boto3
import json
import logging
import os
import paramiko

print ('loading function ...')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    ec2 = boto3.client('ec2')
    message = event['Records'][0]['Sns']['Message']
    messagejson = json.loads(message)
    id = messagejson['Trigger']['Dimensions'][0]['value']
    target_instance = ec2.describe_instances(InstanceIds=[id])
    host = target_instance['Reservations'][0]['Instances'][0]['PublicDnsName']
    print("From SNS: " + message)
    print("The isntance id is:" + id)
    print("hostname is  " + host)
    key = paramiko.RSAKey.from_private_key_file("key")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("connecting to " + host)
    client.connect(host, username='alert',port=22, password=None ,pkey=key)
    print ("connected!")
    commands = ["cd /home ; sudo bash script.sh"]
    for command in commands:
	    print ("Executing {}".format( command ))
	    stdin , stdout, stderr = client.exec_command(command)
            print (stdout.read())
	    print( "Errors")
    	    print (stderr.read())
            client.close()
    return { 
        'message' : 'rebooted server'
    } 
