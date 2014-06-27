#!/usr/bin/env python
from setuptools import setup, find_packages
 
setup(name='d-dot',
      author='toozoofoo',
      author_email='toozoofoo@gmail.com',
      description='',
      version='0.1',
      url='http://github.com/fay/d-dot',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Framework :: Django',
      ],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
