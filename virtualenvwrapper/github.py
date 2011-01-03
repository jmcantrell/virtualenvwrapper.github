import logging
import os
import subprocess

import pkg_resources

log = logging.getLogger(__name__)

def run(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    p.wait()
    return p

def get_url(project):
    p = run('git', 'config', '--global', 'github.user')
    try:
        user = tuple(p.stdout)[0].strip()
    except (TypeError, IndexError):
        user = os.environ.get('VIRTUALENVWRAPPER_GITHUB_USER', os.environ.get('USER'))
    if not user:
        log.error('Set USER or VIRTUALENVWRAPPER_GITHUB_USER')
        return None
    url = 'git@github.com:{user}/{project}.git'.format(user=user, project=project)
    return url

def template(args):
    project = args[0]
    url = get_url(project)
    if url:
        log.info('Cloning %s', url)
        subprocess.call(['git', 'clone', url, 'src'], shell=False)
    return
