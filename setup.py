from distutils.core import setup

setup(
    name="nicosearch",
    py_modules=['nicosearch'],
    version="0.2.1",
    license='MIT License',
    download_url="https://github.com/ymizushi/nicosearch/archive/master.zip",
    platforms=['POSIX'],
    description="https://github.com/ymizushi/nicosearch",
    author="ymizushi",
    author_email="mizushi@gmail.com",
    url="https://github.com/ymizushi/nicosearch",
    keywords=["search", "niconico", "library"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development",
    ],
    long_description="The wrapper library for niconico search API with python."
)
