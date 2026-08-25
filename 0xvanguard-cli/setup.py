from setuptools import setup, find_packages

setup(
    name="0xvanguard-cli",
    version="1.0.0",
    description="CLI to manage 35 cybersecurity repos — AI Security, Tools, Education, Productivity",
    author="0xvanguard",
    author_email="darknetmdb.444@gmail.com",
    url="https://github.com/0xvanguard",
    py_modules=[],
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "0xv=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
    ],
)
