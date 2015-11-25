# tealeaf
A Modular CloudWatch Python Feeder



#IAM Profile

YOu will need a policy like this:

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


# install
unpack in /opt/tealeaf

add cron job

    */5 * * * * /opt/tealeaf/cron.py