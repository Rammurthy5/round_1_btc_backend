from setuptools import setup, find_packages
import os

version = '1.0'

base_dir = os.path.dirname(__file__)


setup(
      name='btc-calculator-redis-celery-django',
      version=version,
      description='Allows to get quotes on latest BTC / USD updates from Stock market',
      long_description=open(os.path.join(base_dir, "README.md")).read(),
      long_description_content_type="text/markdown",
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'
      ],
      keywords='btc-calculator-redis-celery-django',
      author='Team Rainbow',
      author_email='dummyemail@email.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      dependency_links=[],
      install_requires=[
          "asgiref==3.3.1",
          "coverage==6.0.2",
          "Django==3.1.7",
          "djangorestframework",
          "pytz==2021.1",
          "python-dotenv==0.19.1",
          "sqlparse==0.4.1",
          "psycopg2-binary",
          "celery==5.0.5",
          "redis==3.5.3",
          "requests"
      ]
)
