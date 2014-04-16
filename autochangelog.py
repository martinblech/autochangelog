#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import subprocess


def get_tags():
    return subprocess.check_output('git tag'.split()).split()


def get_commits(a, b):
    if a:
        rng = '{}..{}'.format(a, b)
    else:
        rng = b
    return subprocess.check_output(
        'git log --pretty=%s {}'.format(rng).split()
    ).split('\n')

reverse_tags = get_tags() + ['HEAD']
reverse_tags.reverse()
reverse_tags = reverse_tags

print('CHANGELOG')
print('='*len('CHANGELOG'))
print()

for (index, tag) in enumerate(reverse_tags):
    print(tag)
    print('-' * len(tag))

    if index + 1 < len(reverse_tags):
        prev_tag = reverse_tags[index + 1]
    else:
        prev_tag = None
    commits = get_commits(prev_tag, tag)
    if commits:
        print()

    for commit in commits:
        if not commit or commit.lower().find('bump') != -1:
            continue
        print('* ' + commit)

    print()
