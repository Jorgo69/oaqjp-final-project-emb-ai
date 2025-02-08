from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    description='A package for detecting emotions in text',
    author='Votre Nom',
    author_email='votre.email@example.com',
    url='https://github.com/votre-nom/EmotionDetection',
    install_requires=[
        'requests',
    ],
)