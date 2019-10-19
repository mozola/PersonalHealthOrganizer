import sys
from distutils.core import setup

def main():
    setup(
        name="personal health organizer",
        description="Project created to organize to manage diets",
        install_requires=[
            "django-admin",
        ],
    )


if __name__ == "__main__":
    main()

