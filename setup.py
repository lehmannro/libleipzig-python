# Copyright (C) 2009, 2010 Robert Lehmann

from distutils.core import setup
import os.path
import libleipzig

setup(name='libleipzig',
      version=libleipzig.__version__,
      description="wortschatz.uni-leipzig.de binding",
      long_description=open(os.path.join(os.path.dirname(__file__),
          "README.rst")).read(),
      url="http://github.com/lehmannro/libleipzig-python/",
      author="Robert Lehmann",
      author_email="libleipzig@robertlehmann.de",
      license="GPLv3",
      packages=['libleipzig', 'libleipzig.test'],
      package_dir={'libleipzig.test': "tests"},
      package_data={'libleipzig': ["README.rst", "manual.html"]},
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: German',
          'Topic :: Text Processing :: Linguistic',
        ],
)
