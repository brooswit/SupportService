"""aws module

Wrapper for the AWS boto SDK
"""
import os
import time
import boto3

class AwsApi():
    """Interface to AWS API"""
    BUNDLE_ID = "nano_2_0"
    AVAILABILITY_ZONE = "us-west-2a"

    def __init__(self, logger, accessKey=None, secret=None, keyPairName=None):
        """Instantiate a new LightSailApi instance. 

        :param accessKey: AWS Access Key ID
        :param secret: AWS Secret Access Key
        """
        self.accessKey = accessKey
        self.secret = secret
        self.keyPairName = keyPairName
        self.region = os.environ.get('AWS_DEFAULT_REGION')
        self.hostedZoneId = os.environ.get('AWS_HOSTED_ZONE_ID')
        self.logger = logger
        self.client = boto3.client('lightsail')
        self.dns = boto3.client('route53')
    
    @staticmethod
    def _format_ip(hostname):
        return "{0}-staticIP".format(hostname)

    def _ip_match(self, hostname):
        static_ip_name = self._format_ip(hostname)
        try:
            static_ip = self.client.get_static_ip(staticIpName=static_ip_name)
        except self.client.exceptions.NotFoundException:
            return False
        return static_ip['staticIp']['ipAddress'] == self.getInstanceIp(hostname)

    def setStaticIP(self, hostname):
        """Allocate and Attach StaticIP to Instance

        :param hostname: hostname for instance.
        """
        staticIPName = "{0}-staticIP".format(hostname)

        try:
            staticIP = self.client.get_static_ip(
                staticIpName = staticIPName
            )
        except:
            staticIP = self.client.allocate_static_ip(
                staticIpName = staticIPName
            )

        response = self.client.attach_static_ip(
            staticIpName = staticIPName,
            instanceName = hostname
        )
        return response

    def upsertDnsRecord(self, hostname):
        """Create or Update DNS Record for Instance.
        
        :param instanceIp: IP address of new instnace.
        :param hostname: hostname to use for new instance.
        """
        response = self.dns.change_resource_record_sets(
            HostedZoneId=self.hostedZoneId,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': hostname,
                            'Type': 'A',
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': self.getInstanceIp(hostname)
                                }
                            ]
                        }
                    }
                ]
            }
        )

        self.logger.debug(response)
        return response

    def getCentosBlueprint(self):
        """Get first CentOS Blueprint."""
        resp = self.client.get_blueprints(
            includeInactive=False
        )
        blueprints = [x['blueprintId'] for x in resp['blueprints'] if x['name'] == 'CentOS']
        return blueprints[0]

    def getUserData(self):
        """Return Init Script for New Instances."""
        with open('scripts/init.sh', 'r') as initScript:
            data = initScript.read()
            return data

    def getInstanceIp(self, instanceName):
        """Return IP address for instance.

        :param instanceName: name of LightSail isntance
        """
        response = self.client.get_instance(instanceName=instanceName)

        while ('publicIpAddress' not in response['instance']) or (len(response['instance']['publicIpAddress']) < 0):
            self.logger.info("IP for {0} not yet assigned, sleeping".format(instanceName))
            time.sleep(1)
            response = self.client.get_instance(instanceName=instanceName)

        return response['instance']['publicIpAddress']

    def provisionInstance(self, hostname):
        """Create new Lightsail Instance.

        :param hostname: hostname to use 
        """
        response = self.client.create_instances(
            instanceNames=[
                hostname,
            ],
            availabilityZone = self.AVAILABILITY_ZONE,
            blueprintId = self.getCentosBlueprint(),
            bundleId = self.BUNDLE_ID,
            userData = self.getUserData(),
            keyPairName = self.keyPairName
        )
        self.logger.info('Creating new instance called {0}'.format(hostname))
        return response

    def upsert_instance(self, hostname):
        """Upsert Lightsail Instance 

        Check to see if instance exists, if not 
        create a new instance. 

        :param hostname: hostname to check
        """
        try:
            instance = self.client.get_instance(instanceName=hostname)
            self.logger.info("Instance {0} already exists.".format(hostname))
        except self.client.exceptions.NotFoundException:
            self.provisionInstance(hostname)