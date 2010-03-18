# coding=utf-8
from setuptools import setup, find_packages
import os

from version import get_version

setup(name='abel.greeting',
      version=get_version(),
      description="ABEL Change Greeting",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
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
      keywords='abel candidate',
      author='Michael JasonSmith',
      author_email='mpj17@onlinegroups.net',
      url='http://abel.ac.nz',
      license='other',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['abel',],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'Products.XWFCore',
          'Products.GSContent',
          'gs.skin.abel.base',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

