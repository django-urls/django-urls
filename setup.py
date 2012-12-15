from setuptools import setup, find_packages


setup(
    name='django-urls',
    version='0.0.1',
    description='Ease the management of URL patterns and views via the Django admin.',
    author='Zach Borboa',
    author_email='zachborboa@gmail.com',
    url='https://github.com/django-urls/django-urls',
    license='BSD',
    packages=find_packages(exclude=('example', 'tests')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
