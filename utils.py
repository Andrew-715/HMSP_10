import json


def load_candidates():
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for value in load_candidates():
        if pk == value['pk']:
            return value

    return 'Not found'


def get_by_skill(skill_name):
    suitable_candidate = []

    for value in load_candidates():
        if skill_name.lower() in value['skills'].lower().split(', '):
            suitable_candidate.append(value)

    return suitable_candidate
