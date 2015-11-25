# tealeaf
A Modular CloudWatch Python Feeder

#Modules
Only memory has been completed.

#IAM Profile

You will need a policy like this:

    {
    "Statement": [
    {
    "Action": [
    "cloudwatch:ListMetrics",
    "cloudwatch:GetMetricStatistics",
    "cloudwatch:PutMetricData",
    "autoscaling:DescribeAutoScalingInstances"
    ],
    "Effect": "Allow",
    "Resource": "*"
    }
    ]
    }


#Build

    virtualenv venv -p /usr/local/Cellar/python/2.7.10_2/
    source venv/bin/activate
    pip install -r requirements.txt
    

#Tested Systems
- Mac to a certian extent for testing only
- AWS Linux


#Install
Unpack in /opt/tealeaf
Copy config.yml.example to config.yml
Update your region in the config.yml
Add the IAM role to your instance.
Add cron job

    */5 * * * * /opt/tealeaf/cron.sh