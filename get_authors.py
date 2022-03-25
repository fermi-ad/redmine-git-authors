#!/usr/bin/env python3

"""Get the list of unique authors and contributors from Redmine."""

import json
from pathlib import Path
import subprocess


names = set()
output_path = Path('./authors.txt')


def xlat_with(input_dict):
    """Translate the author name."""
    input_keys = input_dict.keys()
    return lambda v: v if v not in input_keys else input_dict[v]

def mk_key(combined_name):
    """Make a key from the author's name."""
    try:
        [first_name, last_name] = combined_name.split()
    except ValueError as errormsg:
        print(errormsg, '\n', combined_name)
        # ! is a low value in the ASCII table
        # This filters the author names that need to be fixed to the top
        return ['!FIX', combined_name]

    return [last_name, first_name]

with open('projects.json', encoding='utf8') as f_projects, \
        open('usernames.json', encoding='utf8') as f_usernames:

    projects = json.load(f_projects)
    usernames_map = json.load(f_usernames)
    usernames = usernames_map.keys()

    for project in projects.keys():
        for repo in projects[project]:
            result = subprocess.run([
                'ssh', '-tx', f'p-{project}@cdcvs.fnal.gov',
                f'git -C /cvs/projects/{repo} log --pretty=\'%an%n%cn\'',
                '|', 'sort', '-u'],
                stdout=subprocess.PIPE, check=True, encoding='utf8')

            if result.returncode != 0:
                print('Return code', result.returncode, f'{project}/{repo} failed.')
                continue

            if result.stdout.startswith('fatal:'):
                print(f'{project}/{repo} failed.')
                print(result.stdout)
                continue

            results = result.stdout.splitlines()

            subbed_names = map(xlat_with(usernames_map), results)
            names |= set(subbed_names)

with open(output_path, 'w', encoding='utf8') as f:
    for name in sorted(names, key=mk_key):
        f.write(f'{name}\n')

    print('Output author names to', output_path.absolute())
