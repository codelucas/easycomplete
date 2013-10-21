from distutils.core import setup

setup(
    name='easycomplete',
    version='0.0.1',
    packages=['easycomplete'],
    package_data={'': ['suggestions.txt', 'english_lib.txt']},
    url='http://codelucas.com',
    license='MIT',
    author='Lucas Ou-Yang',
    author_email='lucasyangpersonal@gmail.com',
    description='A package that returns an autocomplete mapping in python dictionary '+\
                'form. Utilizes google\'s autocomplete and the english dictionary.'
)