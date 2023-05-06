import unittest
import pickle

from fds import fds

class TestFDs(unittest.TestCase):
    def setUp(self):
        self.f = fds.FDs()

    def tearDown(self):
        del self.f

    def test_initialization(self):
        self.assertEqual(self.f.fds, [])
        self.assertEqual(self.f.attributes, set())

    def test_init1(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.assertEqual(self.f.fds, [[{'a'}, {'b'}]])
        self.assertEqual(self.f.attributes, {'a', 'b'})

    def test_init2(self):
        self.f.addfd(fds.FDs.mkfd('a', 'bc'))
        self.assertEqual(len(self.f.fds), 2)
        self.assertIn([{'a'}, {'b'}], self.f.fds)
        self.assertIn([{'a'}, {'c'}], self.f.fds)
        self.assertEqual(self.f.attributes, {'a', 'b', 'c'})

    def test_init3(self):
        self.f.addfd(fds.FDs.mkfd('a', 'bcd'))
        self.assertEqual(len(self.f.fds), 3)
        self.assertIn([{'a'}, {'b'}], self.f.fds)
        self.assertIn([{'a'}, {'c'}], self.f.fds)
        self.assertIn([{'a'}, {'d'}], self.f.fds)
        self.assertEqual(self.f.attributes, {'a', 'b', 'c', 'd'})

    def test_init4(self):
        self.f.addfd(fds.FDs.mkfd('a', 'bbb'))
        self.assertEqual(self.f.fds, [[{'a'}, {'b'}]])
        self.assertEqual(self.f.attributes, {'a', 'b'})

    def test_init5(self):
        self.f.addfd(fds.FDs.mkfd('a', 'bbbccc'))
        self.assertEqual(len(self.f.fds), 2)
        self.assertIn([{'a'}, {'b'}], self.f.fds)
        self.assertIn([{'a'}, {'c'}], self.f.fds)
        self.assertEqual(self.f.attributes, {'a', 'b', 'c'})

    def test_init6(self):
        f = fds.FDs(attributes='aaaaaaa')
        self.assertEqual(f.attributes, {'a'})

    def test_init7(self):
        f = fds.FDs(attributes='aaaaaaa',
                    fds=[fds.FDs.mkfd('a', 'b'),
                         fds.FDs.mkfd('b', 'c'),
                         fds.FDs.mkfd('c', 'd')])
        self.assertEqual(f.attributes, {'a', 'b', 'c', 'd'})
        self.assertEqual(len(f.fds), 3)
        self.assertIn([{'a'}, {'b'}], f.fds)
        self.assertIn([{'b'}, {'c'}], f.fds)
        self.assertIn([{'c'}, {'d'}], f.fds)
        del f

    def test_init8(self):
        f = fds.FDs(attributes='aaaaaaa',
                    fds=[fds.FDs.mkfd('a', 'b'),
                         fds.FDs.mkfd('b', 'c'),
                         fds.FDs.mkfd('b', 'c'),
                         fds.FDs.mkfd('c', 'd')])
        self.assertEqual(f.attributes, {'a', 'b', 'c', 'd'})
        self.assertEqual(len(f.fds), 3)
        self.assertIn([{'a'}, {'b'}], f.fds)
        self.assertIn([{'b'}, {'c'}], f.fds)
        self.assertIn([{'c'}, {'d'}], f.fds)
        del f

    def test_consolidate1(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        c = self.f.consolidate()
        self.assertEqual(len(c), 1)
        self.assertIn([{'a'}, {'b', 'c'}], c)

    def test_consolidate2(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        c = self.f.consolidate()
        self.assertEqual(len(c), 1)
        self.assertIn([{'a'}, {'d', 'b', 'c'}], c)

    def test_consolidate3(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        self.f.addfd(fds.FDs.mkfd('b', 'd'))
        c = self.f.consolidate()
        self.assertEqual(len(c), 2)
        self.assertIn([{'a'}, {'d', 'b', 'c'}], c)
        self.assertIn([{'b'}, {'d'}], c)

    def test_consolidate4(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        self.f.addfd(fds.FDs.mkfd('b', 'd'))
        self.f.addfd(fds.FDs.mkfd('d', 'b'))
        c = self.f.consolidate()
        self.assertEqual(len(c), 3)
        self.assertIn([{'a'}, {'d', 'b', 'c'}], c)
        self.assertIn([{'b'}, {'d'}], c)
        self.assertIn([{'d'}, {'b'}], c)

    def test_attrclosure1(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        c = self.f.attrclosure('a')
        self.assertEqual(len(c), 2)
        self.assertEqual(c, {'b', 'c'})

    def test_attrclosure2(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        c = self.f.attrclosure('ab')
        self.assertEqual(len(c), 2)
        self.assertEqual({'c', 'd'}, c)

    def test_attrclosure3(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        self.f.addfd(fds.FDs.mkfd('b', 'd'))
        c = self.f.attrclosure('cd')
        self.assertEqual(len(c), 0)

    def test_attrclosure4(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('a', 'c'))
        self.f.addfd(fds.FDs.mkfd('a', 'd'))
        self.f.addfd(fds.FDs.mkfd('b', 'd'))
        self.f.addfd(fds.FDs.mkfd('d', 'b'))
        c = self.f.attrclosure('abd')
        self.assertEqual(len(c), 1)
        self.assertEqual({'c'}, c)

    def test_attrclosure5(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('b', 'c'))
        self.f.addfd(fds.FDs.mkfd('c', 'd'))
        self.f.addfd(fds.FDs.mkfd('d', 'a'))
        self.f.addfd(fds.FDs.mkfd('d', 'b'))
        c = self.f.attrclosure('a')
        self.assertEqual(len(c), 3)
        self.assertEqual({'b', 'c', 'd'}, c)

    def test_closure1(self):
        self.f.addfd(fds.FDs.mkfd('a', 'b'))
        self.f.addfd(fds.FDs.mkfd('bc', 'e'))
        self.f.addfd(fds.FDs.mkfd('ed', 'a'))
        fdc = self.f.fdclosure()

        expected = [({'a'}, {'b'}, None),
                    ({'a', 'c'}, {'b', 'e'}, None),
                    ({'a', 'd'}, {'b'}, None),
                    ({'a', 'e'}, {'b'}, None),
                    ({'c', 'b'}, {'e'}, None),
                    ({'d', 'e'}, {'a', 'b'}, None),
                    ({'a', 'c', 'd'}, {'b', 'e'}, 'k'),
                    ({'a', 'c', 'b'}, {'e'}, None),
                    ({'a', 'c', 'e'}, {'b'}, None),
                    ({'a', 'd', 'e'}, {'b'}, None),
                    ({'c', 'b', 'd'}, {'a', 'e'}, 'k'),
                    ({'c', 'd', 'e'}, {'a', 'b'}, 'k'),
                    ({'b', 'd', 'e'}, {'a'}, None),
                    ({'a', 'c', 'b', 'd'}, {'e'}, 's'),
                    ({'a', 'c', 'd', 'e'}, {'b'}, 's'),
                    ({'c', 'b', 'd', 'e'}, {'a'}, 's')]
        self.assertEqual(len(fdc), len(expected))
        for f in expected:
            self.assertIn(f, fdc)

    def test_closure2(self):
        f = fds.FDs(attributes='abcdef',
                    fds=[fds.FDs.mkfd('a', 'b'),
                         fds.FDs.mkfd('c', 'd')])
        fdc = f.fdclosure()
        expected = [({'c'}, {'d'}, None),
                    ({'a'}, {'b'}, None),
                    ({'d', 'a'}, {'b'}, None),
                    ({'b', 'c'}, {'d'}, None),
                    ({'e', 'c'}, {'d'}, None),
                    ({'c', 'a'}, {'d', 'b'}, None),
                    ({'c', 'f'}, {'d'}, None),
                    ({'e', 'a'}, {'b'}, None),
                    ({'f', 'a'}, {'b'}, None),
                    ({'d', 'c', 'a'}, {'b'}, None),
                    ({'d', 'a', 'e'}, {'b'}, None),
                    ({'d', 'f', 'a'}, {'b'}, None),
                    ({'e', 'b', 'c'}, {'d'}, None),
                    ({'b', 'c', 'a'}, {'d'}, None),
                    ({'b', 'c', 'f'}, {'d'}, None),
                    ({'e', 'c', 'a'}, {'d', 'b'}, None),
                    ({'e', 'c', 'f'}, {'d'}, None),
                    ({'f', 'c', 'a'}, {'d', 'b'}, None),
                    ({'e', 'f', 'a'}, {'b'}, None),
                    ({'d', 'c', 'a', 'e'}, {'b'}, None),
                    ({'f', 'd', 'c', 'a'}, {'b'}, None),
                    ({'d', 'f', 'a', 'e'}, {'b'}, None),
                    ({'e', 'b', 'c', 'a'}, {'d'}, None),
                    ({'e', 'b', 'c', 'f'}, {'d'}, None),
                    ({'f', 'b', 'c', 'a'}, {'d'}, None),
                    ({'f', 'e', 'c', 'a'}, {'d', 'b'}, 'k'),
                    ({'f', 'd', 'c', 'a', 'e'}, {'b'}, 's'),
                    ({'f', 'e', 'b', 'c', 'a'}, {'d'}, 's')]

        self.assertEqual(len(fdc), len(expected))
        for f in expected:
            self.assertIn(f, fdc)

    def test_closure3(self):
        f = fds.FDs(attributes = 'abcde',
                    fds=[fds.FDs.mkfd('b', 'a'),
                         fds.FDs.mkfd('ac', 'e'),
                         fds.FDs.mkfd('ed', 'b')])
        fdc = f.fdclosure()
        expected = [({'b'}, {'a'}, None),
                    ({'d', 'e'}, {'a', 'b'}, None),
                    ({'d', 'b'}, {'a'}, None),
                    ({'c', 'a'}, {'e'}, None),
                    ({'c', 'b'}, {'e', 'a'}, None),
                    ({'e', 'b'}, {'a'}, None),
                    ({'d', 'c', 'e'}, {'a', 'b'}, 'k'),
                    ({'d', 'c', 'a'}, {'e', 'b'}, 'k'),
                    ({'d', 'c', 'b'}, {'e', 'a'}, 'k'),
                    ({'d', 'a', 'e'}, {'b'}, None),
                    ({'d', 'e', 'b'}, {'a'}, None),
                    ({'e', 'c', 'b'}, {'a'}, None),
                    ({'c', 'a', 'b'}, {'e'}, None),
                    ({'d', 'c', 'a', 'e'}, {'b'}, 's'),
                    ({'d', 'c', 'e', 'b'}, {'a'}, 's'),
                    ({'d', 'c', 'a', 'b'}, {'e'}, 's')]

        self.assertEqual(len(fdc), len(expected))
        for f in expected:
            self.assertIn(f, fdc)

    def test_closure4(self):
        f = fds.FDs(fds=[fds.FDs.mkfd('P', 'DSLUATEIF'),
                         fds.FDs.mkfd('DS', 'PLUATEIF'),
                         fds.FDs.mkfd('LU', 'PDSATEIF'),
                         fds.FDs.mkfd('A', 'U')])

        fdc = f.fdclosure()
        with open('tests/test-closure-4.txt', 'rb') as x:
            fdce = pickle.loads(x.read())

        self.assertEqual(len(fdc), len(fdce))
        for e in fdce:
            self.assertIn(e, fdc)

        c = f.consolidate()
        expected = [[{'P'}, {'E', 'A', 'S', 'U', 'D', 'I', 'T', 'L', 'F'}],
                    [{'D', 'S'}, {'I', 'E', 'T', 'P', 'A', 'L', 'U', 'F'}],
                    [{'L', 'U'}, {'I', 'S', 'E', 'T', 'P', 'A', 'F', 'D'}],
                    [{'A'}, {'U'}]]
        self.assertEqual(len(c), len(expected))
        for e in expected:
            self.assertIn(e, c)

        g = fds.FDs()
        for mc in f.minimalCover():
                g.addfd((mc[0], mc[1]))

        gdc = g.fdclosure()
        self.assertEqual(len(gdc), len(fdce))
        for e in fdce:
            self.assertIn(e, gdc)

        self.assertFalse(g.isbcnf())
        self.assertTrue(g.is3nf())
