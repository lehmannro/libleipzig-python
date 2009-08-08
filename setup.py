# Copyright (C) 2009 Robert Lehmann

from distutils.core import setup
import libleipzig

setup(name='libleipzig',
      version=libleipzig.__version__,
      description="wortschatz.uni-leipzig.de binding",
      long_description=file("README.rst").read(),
      url="http://github.com/lehmannro/libleipzig-python/",
      author="Robert Lehmann",
      author_email="libleipzig@robertlehmann.de",
      license="GPLv3",
      packages=['libleipzig'],
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: German',
          'Topic :: Text Processing :: Linguistic',
        ],
)
