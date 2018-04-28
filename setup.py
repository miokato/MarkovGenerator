from distutils.core import setup


setup(
    name='MarkovGenerator',
    version='0.0.1',
    description='Text generator using the Markov model',
    author='Mio Kato',
    author_email='miokato07@gmail.com',
    url='https://github.com/miokato/MarkovGenerator',
    install_requires=['numpy', 'mecab-python3'],
    py_modules=['generator'],
)