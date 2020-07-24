from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='typewriter_print',
      version='0.1',
      author='Raj Dholakia',
      author_email='raj9dholakia@gmail.com',
      url='https://gtihub.com/radroid',
      license='MIT open-source licence',
      description='typewriter animation print package',
      keywords=['typewriter effect', 'print function', 'animation', 'command-line'],
      long_description=long_description,
      packages=['TypewriterPrint'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 1 - Alpha',
          'Intended Audience :: Python Developers',
          'License :: MIT',
          'Operating System :: Linux/MacOs',
          'Programming Language :: Python',
          'Topic :: Desktop Environment'
      ]
      )
