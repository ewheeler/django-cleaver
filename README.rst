Django views and templates for use with `Cleaver <https://github.com/ryanpetrello/cleaver>`_

Cleaver includes `bottle <http://bottlepy.org/>`_ and a 
`simple web interface <https://github.com/ryanpetrello/cleaver/tree/master/cleaver/reports/web>`_  to review experiment results.


If you're using Cleaver with a Django app, it seems silly to run a separate 
wsgi app just for the experiments overview. So here is a port of the bottle 
interface to Django to include in your project.

BONUS: includes a view that returns experiment results in JSON
