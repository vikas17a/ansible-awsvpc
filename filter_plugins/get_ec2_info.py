from jinja2.utils import soft_unicode

'''
USAGE:
 - debug:
     msg: "{{ ec2.results | get_ec2_info('') }}"
'''


class FilterModule(object):
    def filters(self):
        return {
            'get_ec2_info': get_ec2_ids,
        }

def get_ec2_ids(list):
    ec2_ids = []
    for item in list:
        dictonary = {}
        dictonary['az'] = item['item']['az']
        dictonary['instance_id'] = item['tagged_instances'][0]['id']
        ec2_ids.append(dictonary)
    return ec2_ids
