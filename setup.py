from setuptools import setup, find_packages

__author__ = 'Paola Soto'


setup(
    name='optimization',
    version="0.0.1",
    packages=find_packages(),
    author='Paola Soto',
    author_email='paola.soto@udea.edu.co',
    description='Repositorio para el curso de Técnicas de Optimización',
    install_requires=["numpy", "scipy", "jupyter", "matplotlib", "ortools", "wand", "folium"]
)