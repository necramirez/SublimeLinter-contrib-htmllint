#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Nikki Erwin Carpio Ramirez
# Copyright (c) 2016 Nikki Erwin Carpio Ramirez
#
# License: MIT
#

"""This module exports the Htmllint plugin class."""

from SublimeLinter.lint import NodeLinter


class Htmllint(NodeLinter):
    """Provides an interface to htmllint."""

    defaults = {
        'selector': 'text.html'
    }
    npm_name = 'htmllint-cli'
    cmd = ('htmllint', '@')
    config_file = ('--rc', '.htmllintrc')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.7'
    regex = r'^.+: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+)'
