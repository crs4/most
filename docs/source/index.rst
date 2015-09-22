.. MOST documentation master file, created by
   sphinx-quickstart on Thu Jul 10 17:16:13 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
Welcome to MOST's documentation!
================================

The MOST project aims to achieve an open, modular and scalable solution for the creation, execution and management of remote clinical consultations with direct interaction between specialists.

The project consists of a set of frameworks that deal with different aspects and technologies useful for the creation of telemedicine applications.

In addition to the frameworks, the project contains a number of helper modules, that should ease developers to build telemedicine applications focusing only on high value-added functionality.

Frameworks
==========

- `Voip <http://most-voip.readthedocs.org/en/latest/>`_: a fast and lightweight library created for handling VOIP sessions;
- `Streaming  <https://github.com/crs4/most-streaming>`_: a library for managing audio/video streams;
- `Visualization  <https://github.com/crs4/most-visualization>`_: a library for providing mobile applications with visual widgets for interacting with A/V streams;
- `Demographics <http://most-demographics.readthedocs.org/en/latest/>`_: a Django application for patients management;
- `Report  <https://github.com/crs4/most-report>`_: a library for managing clinical models;
- `MedicalRecords  <https://github.com/crs4/most-medicalrecords>`_: a frontend REST api for accessing to demographics and clinical data of patients;
- `Demo  <https://github.com/crs4/most-demo>`_: a DEMO Application showing the main features of the MOST frameworks.


Helpers
=======

- :doc:`users/most_user`:  a Django application for creation and management of administrative users;
- :doc:`users/clinician_user`:  a Django application for creation and management of clinician users;
- :doc:`users/task_group`:  a Django application for creation and management of technical and clinician task groups;
- :doc:`authentication/authentication`:  a consumer/producer library for user authentication based on oauth2 protocol.



Project TOC
===========

.. toctree::
   :maxdepth: 2

   modules
   helpers
   license
   authors


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
