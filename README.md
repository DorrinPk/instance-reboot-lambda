# instance-reboot-lambda
reboot an instance that is triggered off SNS via lambda

### Story time! 

This was inspired by a bug in a developer's code. The cycle was app crashes -> manually run a script to ssh + reboot 

This was tiresome as there was no idication of when app was about to crash and I couldn't have any agents on the box for monitoring. 

Devops to the rescue! I noticed this pattern while looking at EC2 graphs : as network packets drop to X, app crashes shortly after. So created a SNS topic that alerts on `lower than X` network packets. This lambda runs when the SNS topic triggers. 

### Development notes 

As this lambda depends on Crypto libraries, it's important to compile and package the lambda on Amazonlinux. I deploy mine from a docker container. 