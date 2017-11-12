from random import shuffle
import yaml


def print_parts(parts):
    for key, part in enumerate(parts):
        target = part['target'].get('name') if part.get('target') is not None else ''
        print('{0} => {1}'.format(part['name'], target))


def can_gift(source, target):
    if source == target:
        return False
    if 'group' in source and source.get('group') == target.get('group'):
        return False
    if 'source' in target:
        return False
    return True


with open('./participants.yml') as file:
    data = yaml.safe_load(file)
    parts = data['participants']
    shuffle(parts)
    for key, part in enumerate(parts):
        for c in range(key + 1, key + len(parts)):
            target_key = c % len(parts)
            target_part = parts[target_key]
            if can_gift(part, target_part):
                parts[target_key]['source'] = part
                parts[key]['target'] = target_part
                break
    print_parts(parts)
