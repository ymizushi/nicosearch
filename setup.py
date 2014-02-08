from distutils.core import setup

setup(
      name = "nicosearch",
      version = "0.0.1",
      license = open('./LICENSE').read(),
      platforms = ['POSIX'],
      description = "https://github.com/ymizushi/nicosearch",
      author = "ymizushi",
      author_email = "mizushi@gmail.com",
      url = "https://github.com/ymizushi/nicosearch",
      keywords = ["search", "niconico"],
      classifiers = [
                     'License :: OSI Approved :: MIT License',
                     "Programming Language :: Python",
                     "Development Status :: 4 - Beta",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Topic :: Utilities",
                     "Topic :: Software Development",
                     ],
      long_description = open('README.md').read()
      )
