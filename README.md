vpc
=========

A role to create AWS VPC enviornment

Requirements
------------

```python >= 2.6```
```boto```

Role Variables
--------------
```
VPC_NAME: This variable defines name of VPC
VPC_REGION: Region for VPC
VPC_CIDR: CIDR of VPC
VPC_CLASS_DEFAULT: CLASS of above CIDR
ENVIRONMENT: Enviornment name
KEY_PAIR: key to be used for booting up nat instances

vpc_nat_instance_type: size of nat instance
vpc_nat_instance_id: nat instance ami ids in dict with key as region

vpc_subnets: defination of subnets goes here
```

