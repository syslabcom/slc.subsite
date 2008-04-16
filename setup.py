from setuptools import setup, find_packages

version = '0.1'

setup(name='slc.subsite',
      version=version,
      description="Make a Folder behave like a Subsite",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='subsite skin',
      author='Syslab.com GmbH',
      author_email='info@syslab.com',
      url='http://svn.plone.org/svn/collective/slc.subsite',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['slc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
