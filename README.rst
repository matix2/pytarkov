pytarkov
==========
.. image:: https://img.shields.io/pypi/v/pytarkov.svg
   :target: https://pypi.python.org/pypi/pytarkov
   :alt: PyPI version info

Python wrapper for Escape from Tarkov API provided by https://tarkov-market.com

Installing
----------
**Python 3.6 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U pytarkov

    # Windows
    py -3 -m pip install -U pytarkov

Getting API key
---------------
You can get your API key from `here <https://tarkov-market.com/dev/api>`_.


Quick Example
--------------

.. code:: py

    import pytarkov

    client = pytarkov.PyTarkov("api-key-here")
    item = client.get_item_by_name("bitcoin")
    print(f"{item.name()} price: {item.price()}")