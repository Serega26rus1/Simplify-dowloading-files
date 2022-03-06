import setuptools

with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Simplify_downloading_files_TG",
    version = "0.0.1",
    author="Zhenya Ovchinnikov",
    description="Simplify downloading files from Telegram for PyTelegramBotAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhenyaGOTL/Simplify-dowloading-files",
    project_urls={
        "Bug Tracker":"https://github.com/ZhenyaGOTL/Simplify-dowloading-files/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Pillow',
        'requests',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)