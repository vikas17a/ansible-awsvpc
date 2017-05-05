from jinja2.utils import soft_unicode

'''
USAGE:
 - debug:
     msg: "{{ vpc.subnets | get_public_subnets_ids('Type','Public') }}"
'''


class FilterModule(object):
    def filters(self):
        return {
            'get_subnets_ids_by_tag': get_subnets_ids_by_tag,
            'get_subnets_ids_by_az' : get_private_subnets_ids_by_az,
        }


def get_subnets_ids_by_tag(list, tag_key, tag_value):
    '''
    Get all subnets with specific tags and value
    '''
    subnets_ids = []
    for item in list:
        subnet_dict = {}
        for key, value in item['subnet']['tags'].iteritems():
            if key == tag_key and value == tag_value:
                subnet_dict['subnet_id'] = item['subnet']['id']
                subnet_dict['az'] = item['subnet']['availability_zone']
                subnets_ids.append(subnet_dict)
    return subnets_ids

def get_private_subnets_ids_by_az(list, az):
    '''
    Get all subnets with specific az
    '''
    subnet_ids = []
    for item in list:
        for key, value in item['subnet']['tags'].iteritems():
            if key == 'Type' and value == 'Private':
                if item['subnet']['availability_zone'] == az:
                    subnet_ids.append(item['subnet']['id'])
    return subnet_ids

