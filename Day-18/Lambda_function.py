# Through this function EC2 instance, EBS, Snapshot will be if not in use.

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

# Get all EBS snapshots
response = ec2.describe_snapshots(OwnerIds=['self'])

# Get all activce EC2 instance IDs 
response = client.describe_instances(filter=[{'name': 'instance-state-name', 'value': ['running']}]
active_instances_ids = set()

for reservation in instances_response['Reservations']:
    for instance in reservation['Instances']:
        active_instance_ids.add(instance['InstanceId'])

# Iterate through each snapshot and delete if it's not attached to any volume or 
for snapshot in response['Snapshots']:
    snapshot_id = snapshot['SnapshotId']
    volume_id = snapshot.get('volumeId')

    if not volume_id:
        # Delete the snapshot if it's not attached to any volume
        ec2.delte_snapshot(SnapshotsId=Snapshot_id)
        print(f"Delete EBS snapshot {snapshot_id} as it's not attached to any volume.")
    else: 
        # check of the volume still exists
        try:
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['volume'][0]['Attachments']  :
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Delted EBS snapshot {snapshot_id} as it was taken from the a volume not attached")
        except ec2.exceptions.ClientError as e:
            if e.response['error']['code'] == 'InvalidVolume.NotFound':
                # The colume associated with the snapshot is not found (it might have been deleted)
                ec2.delete_snapshot(SnapshotID=snapshot_Id)
                print(f'Delete EBS snapshot {snapshot_id} as its associated volume was not found.')
