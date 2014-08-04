===========
Flask-Stats
===========

.. module:: flask.ext.stats

This flask extension automatically provides paging timing and http status code
statistics to statsd.

It will send page timings to `<APP_NAME>.<BLUEPRINT>.<FUNCTION>`, and status
codes to `<APP_NAME>.<BLUEPRINT>.<FUNCTION>.http_XXX`, where XXX is the status
code, i.e 403.

Installation
------------

Install by installing it from the Python Package Index.

.. code-block:: console

    $ pip install Flask-Stats

Configuration
-------------

Flask-Stats uses the following configuration values.

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|


=============================== ========================================================
`STATS_HOSTNAME`                Specifies the host to send statsd values to. Defaults to
                                localhost.
`STATS_PORT`                    Specified the port to send statsd values to. Defaults to
                                8125.
`STATS_BASE_KEY`                The base key to send the stats to. Defaults to the
                                application name.
=============================== ========================================================


API Documentation
-----------------

.. automodule:: flask_stats
    :members:
    :undoc-members:
    :show-inheritance:
