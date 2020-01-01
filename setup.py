#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.install import install
from subprocess import check_call


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        check_call("systemctl daemon-reload".split())
        check_call("systemctl enable kodiMcontrol".split())
        install.run(self)

setup(name='kodiMcontrol',
      version='1.0',
      description='mcontrol Gateway server for kodi',
      author='Tobias D. Oestreicher',
      author_email='lists@oestreicher.com.de',
      url='https://github.com/tobias-d-oe/kodiMcontrol/',
      data_files=[('/etc/kodiMcontrol', ['conf/kodiMcontrol.cfg', 'conf/kodiMcontrolServer.xml']),
                  ('/usr/bin/', ['src/kodiMcontrolServer']),
                  ('/lib/systemd/system/', ['conf/kodiMcontrol.service'])],
      cmdclass={'install': PostInstallCommand,},
     )



