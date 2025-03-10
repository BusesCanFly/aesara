
.. _libdoc_compile_shared:

===========================================
:mod:`shared` - defines aesara.shared
===========================================

.. module:: aesara.compile.sharedvalue
   :platform: Unix, Windows
   :synopsis: defines aesara.shared and related classes
.. moduleauthor:: LISA


.. class:: SharedVariable

    Variable with storage that is shared between the compiled functions that it appears in.
    These variables are meant to be created by registered *shared constructors*
    (see :func:`shared_constructor`).

    The user-friendly constructor is :func:`shared`

    .. method:: get_value(self, borrow=False, return_internal_type=False)

       :param borrow: True to permit returning of an object aliased to internal memory.
       :type borrow: bool

       :param return_internal_type: True to permit the returning of an arbitrary type object used
               internally to store the shared variable.
       :type return_internal_type: bool

       By default, return a copy of the data. If ``borrow=True`` (and
       ``return_internal_type=False``), maybe it will return a copy.
       For tensor, it will always return an `ndarray` by default, so if
       the data is on another device, it will return a copy, but if the data
       is on the CPU, it will return the original data.  If you do
       ``borrow=True`` and ``return_internal_type=True``, it will
       always return the original data, not a copy, but this can be a non-`ndarray`
       type of object.

    .. method:: set_value(self, new_value, borrow=False)

       :param new_value: The new value.
       :type new_value: A compatible type for this shared variable.

       :param borrow: True to use the new_value directly, potentially creating problems
           related to aliased memory.
       :type borrow: bool

       The new value will be seen by all functions using this SharedVariable.

    .. method:: __init__(self, name, type, value, strict, container=None)

        :param name: The name for this variable.
        :type name: None or str

        :param type: The :term:`Type` for this Variable.

        :param value: A value to associate with this variable (a new container will be created).

        :param strict: True -> assignments to ``self.value`` will not be casted
          or copied, so they must have the correct type or an exception will be
          raised.

        :param container: The container to use for this variable.   This should
           instead of the `value` parameter.  Using both is an error.

    .. attribute:: container

        A container to use for this SharedVariable when it is an implicit function parameter.


.. autofunction:: shared

.. function:: shared_constructor(ctor)

    Append `ctor` to the list of shared constructors (see :func:`shared`).

    Each registered constructor `ctor` will be called like this:

    .. code-block:: python

        ctor(value, name=name, strict=strict, **kwargs)

    If it do not support given value, it must raise a `TypeError`.
