========
``pydo``
========

``pydo`` is a ``perl``-inspired command line utility. It adds the ability to
use ``perl``'s ``-n`` (run some code on each line of input) and ``-p`` (run
some code on each line of input, and print the — possibly mutated — line to
stdout) to Python.

For example, to add C-style comments to each line, you could do ``sed -e
s/^/\/\/ /`` (or better, ``sed -e s_^_// _``), or
``pydo -p 'line = "// " + line`` Example::

    % printf 'a\nb\nc\n' | pydo -p 'line = "// " + line'
    // a
    // b
    // c

This is a simple example, meant to illustrate. For more complex tasks, it is
hoped that ``pydo`` is both easier to construct and read, as well as
encouraging more correctness in the result.
