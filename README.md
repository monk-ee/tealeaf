# tealeaf

A Modular CloudWatch Python Feeder

#Modules
Add only the modules you want in the config.yml file.
Only memory has been completed.

Build your own modules based on your custom metrics see the examplemodule.py.


#Namespace
You can change the namespace prefix in the config.yml file


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

#Config

    general:
      region: "ap-southeast-2"
      debug: True
      logfile: 'tealeaf.log'
      namespace_prefix: 'Tea_Leaf_'
    modules:
     - Memory


#Install

Unpack in /opt/tealeaf

Copy config.yml.example to config.yml

Update your region in the config.yml

Add the IAM role to your instance.

Add cron job

    */5 * * * * /opt/tealeaf/cron.sh