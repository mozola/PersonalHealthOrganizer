=======================
PersonalHealthOrganizer
=======================

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://dix.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://travis-ci.org/sphinx-doc/sphinx.svg?branch=master
   :target: https://travis-ci.org/mozola/DIX
   :alt: Build Status (Travis CI)

PHO is a application created to create and manage mutrition plans and
exercise plans. This application is created alike to people who have
active lifestyle or just want to not waste food. 

**PersonalHealthOrganizer is the application dedicated to people who:**

- want to prepare nutrition plan and measure the status
- buy a products dedicated to the plan not random products
- want's to have information about meals to the next day and how to prepare them
- want to prepare plan with informations about single meal calories

**How to run this application on a server?**

To run this application user should clone this repo in a local machine.

.. code-block:: bash
		
	  git clone https://github.com/mozola/PersonalHealthOrganizer.git

After that user should go to created folder. In linux system it will be cd command:

.. code-block:: bash
		
	  cd PersonalHealthOrganizer

The next step will be to run tox command with is responsible for create virtual
environment and run application on specific port.

.. code-block:: bash
		
	  tox -e run-application

**Current features**

- [x] Storage all informations about products and meals

- [x] Ability to create and manage nutrition plans

- [ ] Storage informations about exercices

- [ ] Ability to create exercise plans

- [X] After plan start user should recive information with shoppuing list

- [] Status bar when user create a new plan


**Bellow are presented screens from the program.**

.. image:: http://waldemar.mozola.pl/wp-content/uploads/2019/09/Screenshot-from-2019-09-07-13-29-43-1200x598.png
   :alt: First screen


.. image:: http://waldemar.mozola.pl/wp-content/uploads/2019/09/Screenshot-from-2019-09-07-11-34-33-1-1200x566.png
   :alt: First screen
   
.. image:: http://waldemar.mozola.pl/wp-content/uploads/2019/09/Screenshot-from-2019-09-07-13-30-18-1200x626.png
   :alt: First screen

