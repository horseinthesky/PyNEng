def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    result = []

    for intf in access:
        result.append('interface ' + intf,)
        for command in access_template:
            if command.endswith('access vlan'):
                result.append(' {} {}'.format(command, access[intf]))
            else:
                result.append(' {}'.format(command))
    return result

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
 
    trunk_config = []

    for intf in trunk:
        trunk_config.append('interface {}'.format(intf))
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlans = ','.join(str(vlan) for vlan in trunk[intf])
                trunk_config.append(' {} {}'.format(command, vlans))
            else:
                trunk_config.append(' {}'.format(command))
    return trunk_config

def get_int_vlan_map(config):
    """
    config - название файла конфигурации устройства.

    Функция создаёт словари access и trunk портов access_dist и trunk_dist соответственно.
    """
    access_dist = {}
    trunk_dist = {}

    with open(config) as f:
        f = f.read().replace('\n', '').split('!')
        for el in f:
            if 'access vlan' in el:
                access_dist[el.split()[1]] = int(el.split()[8])
            elif 'trunk' in el:
                trunk_dist[el.split()[1]] = [ int(v) for v in el.split()[10].split(',') ] 
            else:
                pass

    return access_dist, trunk_dist
