#!/usr/bin/env python

import re
import subprocess
import shlex

import psutil
import click
from python_toolbox import caching


@caching.cache()
def get_cmdline(process):
    try:
        return process.cmdline()
    except psutil.AccessDenied:
        return ('',)


@caching.cache()
def get_cwd(process):
    try:
        return process.cwd()
    except psutil.AccessDenied:
        return None


@click.command()
@click.argument('search_str', default='')
@click.option('-k', '--kill', is_flag=True, default=False, help='Should kill the process')
@click.option('-r', '--restart', is_flag=True, default=False, help='Should restart the process')
def ps(search_str, kill, restart):
    python_processes = [process for process in psutil.process_iter() if re.match(r'^python[-.0-9]*w?(:?.exe)?$', process.name())]
    processes = [process for process in python_processes
                 if len(get_cmdline(process)) > 1 and search_str in get_cmdline(process)[1].lower()]

    for process in processes:
        cmdline = get_cmdline(process)
        cwd = get_cwd(process)
        click.echo(' '.join(map(shlex.quote, cmdline)))
        if kill or restart:
            click.echo('killing pid={0}'.format(process.pid))
            process.kill()
        if restart:
            new = subprocess.Popen(cmdline, cwd=cwd)
            click.echo('started new process pid={0}'.format(new.pid))


if __name__ == '__main__':
    ps()
