"""
Mostly allowed syntax in Python 3.5.
"""


async def foo():
    yield 1
    await bar()
    #: E901
    yield from []


# With decorator it's a different statement.
@bla
async def foo():
    yield 1
    await bar()
    #: E901
    yield from []
