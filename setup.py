# coding=utf-8
from setuptools import setup, find_packages
import os

from version import get_version

setup(name='gs.site.change.greeting',
      version=get_version(),
      description="GroupServer Configurable Greeting",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='groupserver greeting',
      author='Michael JasonSmith',
      author_email='mpj17@onlinegroups.net',
      url='http://www.onlinegroups.net',
      license='other',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gs', 'gs.site', 'gs.site.change',],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'Products.XWFCore',
          'Products.GSContent',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

