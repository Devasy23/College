# functional-dependencies

A simple library to compute functional dependencies and other related things.

Class FDs

      FDs(attributes=<attributes>, fds=<fds>)

      mkfd(<attributes>, <dependency>)

        Construct a dependency suitable to be added to FDs


      addfd(fd)

        Add a functional dependency

      consolidate()

        Return a consolidation of all FDs.

      attrclosure(<attributes>)

        Compute an attribute closure()

      fdclosure()

        Return the fdclosure for known FDs

      keys()

        Return the keys for all known FDs

      minimalCover()

        Compute the minimal cover for all known FDs

      isbcnf()
      is3nf()

        Return True or False; is the schema BCNF or 3NF

Testing

  python -m unittest tests/testcases.py