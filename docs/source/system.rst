Level 1: System context architecture
====================================

A System Context diagram provides a starting point, showing how the software system in scope fits into the world around it.

This is a high level abstraction detailing the system, the users of the system, the other systems that it interacts with.

This also serves as a non-technical summary



cmascience
~~~~~~~~~~

.. mermaid::

   graph TB
      1((START)) --> 2(Verify available input data)
      1 --> 3(Import data)
      2 --> 4(Build grids)
      4 --> 5(other step)
      5 --> 6(Archive)
      2 --> 8(other)
      13>Test outputs] --> 9
      9 --> 10(Build visualisation)
      10 --> 11(Archive)
      11 --> 7
      6 --> 7(Build website)
      7 --> 12((END))
