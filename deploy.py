from __future__ import print_function

import os
import re
from argparse import ArgumentParser
from twilio import __version_info__, __version__

def main(version):
    current_version = __version__

    if version is None:
        match = re.search(r'(\d+)$', __version_info__[-1])
        if not match or match.group() is None:
            exit('Unable to auto bump version')

        patch = int(match.group())
        patch += 1

        prefix = __version_info__[-1][:(-1 * len(match.group()))]

        new_patch = '{}{}'.format(prefix, patch)

        version = '.'.join(__version_info__[:-1] + (new_patch, ))

    print('Deploying {} -> {}'.format(current_version, version))

    info = version.split('.')

    init_src = ("__version_info__ = ({version_info})\n"
                "__version__ = '.'.join(__version_info__)\n")
    init_src = init_src.format(version_info=', '.join(["'{}'".format(i) for i in info]))

    print('Updating twilio/__init__.py ... ', end="")
    with open('twilio/__init__.py', 'w') as init_file:
        init_file.write(init_src)
    print('Done')

    new_readme = []

    print('Updating README.md ... ', end="")
    with open('README.md', 'r') as readme:
        for line in readme.readlines():
            if current_version in line:
                line = line.replace(current_version, version)
            new_readme.append(line)

    with open('README.md', 'w') as readme:
        readme.writelines(new_readme)
    print('Done')

    print('git commit version bump')
    os.system('git commit -am "Bumping version to {}"'.format(version))
    os.system('git push')
    print('Done')

    print('Pushing to pypi')
    os.system('make release')
    print('Done')

    print('Adding git tag')
    os.system('git tag {}'.format(version))
    os.system('git push --tags')
    print('Done')

    # TODO: Remove this once 6.x is Generally Available

    print('!' * 80)
    print('! {:^76} !'.format('Go hide latest RC and unhide latest 5.x'))
    print('!' * 80)

    os.system('open "https://pypi.python.org/pypi?:action=pkg_edit&name=twilio"')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('version', nargs='?')
    args = parser.parse_args()

    main(args.version)
