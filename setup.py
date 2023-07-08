from setuptools import setup, find_packages

setup(
    name='KineticLearning',
    version='1.0',
    packages=find_packages(),
    author='Zak Costello, and Hector Garcia Martin',
    author_email='hgmartin@lbl.gov',
    description='A machine learning approach to predict metabolic pathway dynamics from time-series multiomics data',
    url='https://github.com/JBEI/KineticLearning',
    install_requires=['numpy','TPOT','scipy','networkx','matplotlib','pandas','ipython','seaborn','scikit_learn'],
)
