
.. image:: https://github.com/mangolang/cli/workflows/Test%20&%20deploy%20Mango%20CLI/badge.svg
    :target: https://github.com/mangolang/cli/actions

.. image:: https://deps.rs/repo/github/mangolang/cli/status.svg
    :target: https://deps.rs/repo/github/mangolang/cli

.. image:: https://readthedocs.org/projects/mangolang/badge/?version=latest
    :target: https://docs.mangocode.org/en/latest/

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0


Mango CLI utils for compiler
===============================

This repository contains shared code used for automatic building and testing of different parts of the Mango compiler.

Base Docker image
-------------------------------

This repository publishes a Docker image that can be used as a base to build the Mango compiler in a reproducible way::

It is called `mangocode/mango_daily_base` (`on dockerhub`_)

Besides sharing code, this has the benefit of decreasing build times by a lot because dependencies can be pre-installed.

Links
-------------------------------

* `Official website`_
* `Documentation`_
* `Code of conduct and contributing`_

.. _Official website: https://mangocode.org/
.. _`Documentation`: https://docs.mangocode.org/
.. _`Code of conduct and contributing`: https://github.com/mangolang/mango
.. _`on dockerhub`: https://hub.docker.com/repository/docker/mangocode/mango_daily_base/general
