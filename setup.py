from setuptools import find_packages, setup
setup(
    name='clusterysis',
    packages=find_packages(include=['clusterysis']),
    version='0.1.0',
    description='A library for visualizing clusters.',
    author='Gabriel Di Pardi Arruda',
    license='MIT',
    install_requires=['plotly', 'pandas'],
)
