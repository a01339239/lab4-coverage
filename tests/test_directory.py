from unittest import mock, TestCase
from dataclasses import asdict
from random import randint
from typing import Optional
from json import load as jload, dumps as jdumps, JSONDecodeError
from os import SEEK_END
from time import time

from lab3.directory import Directory, Record


class TestDirectoryCases(TestCase):
    """Test decimal to binary conversion works appropriately."""

    def setUp(self):
        """Set new dictionary before each test."""
        self.directory = Directory()

    @staticmethod
    def get_random_record(id_: Optional[str] = None) -> Record:
        """Get a record with random values."""
        randomizer = randint(1, 10)
        return Record(
            id=id_,
            name=f"Name_{randomizer}",
            email=f"email{randomizer}@email.com",
            age=randomizer,
            country_of_origin=f"Country_{randomizer}",
        )

    def test_directory__boundary_conditions(self):
        """
        Test boundary conditions.

        - creating and looking for a record with a custom id.
        - deleting a record that does no exist.
        - looking for records that match the same filter.
        - looking for a record that does not exist.
        - looking for a record without proving email or age.
        """
        # Create and look for record with custom id
        r1 = self.get_random_record(id_="1")
        self.directory.add_record(r1)
        self.assertListEqual(self.directory.look_for_record(email=r1.email), [r1])

        # Delete a record that does not exist
        self.assertEqual(self.directory.delete_record(_id="2"), 0)

        # Look for a record that is repeated
        self.directory.add_record(r1)
        matches = self.directory.look_for_record(email=r1.email, age=r1.age)
        self.assertListEqual(matches, [r1, r1])

        # Look for a record that does not exist
        self.assertListEqual(self.directory.look_for_record(email="nope@email.com"), [])

        # Look for a record without email or age
        self.assertListEqual(self.directory.look_for_record(), [])

    @mock.patch("lab3.directory.pprint")
    def test_directory__inverse_relationships(self, mock_print):
        """
        Test available inverse relationships.

        - add and delete one and multiple records.
        """
        # Add and delete one record
        r1 = self.get_random_record()

        self.directory.add_record(r1)
        self.directory.display_all_records()
        mock_print.assert_called_with([asdict(r1)])

        self.directory.delete_record(r1.id)
        self.directory.display_all_records()
        mock_print.assert_called_with([])

        # Add and delete many records
        recs = [self.get_random_record() for _ in range(10)]
        for rec in recs:
            self.directory.add_record(rec)
        self.directory.display_all_records()
        mock_print.assert_called_with([asdict(rec) for rec in recs])

        for rec in recs:
            self.directory.delete_record(rec.id)
        self.directory.display_all_records()
        mock_print.assert_called_with([])

    @mock.patch("lab3.directory.pprint")
    def test_directory__cross_checking(self, mock_print):
        """
        Cross-checking tests.

        - comparing print arguments with directory.json contents.
        - manually adding records instead of using Directory().add_record().
        """
        # Display directory and reading file
        recs = [self.get_random_record() for _ in range(10)]
        for rec in recs:
            self.directory.add_record(rec)
        self.directory.display_all_records()

        with open("lab3/directory.json", "r") as f:
            json_from_file = jload(f)
        self.assertListEqual(mock_print.call_args[0][0], json_from_file)

        # Manual directory manipulation
        rec = self.get_random_record()
        with open("lab3/directory.json", "rb+") as f:
            f.seek(-1, SEEK_END)
            f.truncate()
            f.write(bytes(f",{jdumps(asdict(rec))}]", encoding="utf-8"))
        self.directory.display_all_records()
        self.assertListEqual(
            mock_print.call_args[0][0], [asdict(r) for r in recs + [rec]]
        )

    def test_directory__error_conditions(self):
        """
        Test error conditions.

        - adding a non-dataclass class as if it were a Record instance.
        - altering the directory.json file and calling Directory().add_record().
        """
        # Add non-dataclass class
        no_record = mock.Mock()
        with self.assertRaises(TypeError):
            self.directory.add_record(record=no_record)

        # Alter the directory.json file
        with open("lab3/directory.json", "rb+") as f:
            f.seek(-1, SEEK_END)
            f.truncate()
        r = self.get_random_record()
        with self.assertRaises(JSONDecodeError):
            self.directory.add_record(r)

    @mock.patch("lab3.directory.pprint")
    def test_directory__performance(self, _):
        """
        Test performance by requiring a maximum execution time.

        - adding many records to directory.
        - displaying many records.
        - deleting many records.
        """
        # Add many records to dir
        recs = [self.get_random_record() for _ in range(10)]
        start = time()
        for rec in recs:
            self.directory.add_record(rec)
        self.assertLessEqual(time() - start, 0.3)

        # Display all the records
        start = time()
        self.directory.display_all_records()
        self.assertLessEqual(time() - start, 0.03)

        # Delete many records from dir
        start = time()
        for rec in recs:
            self.directory.delete_record(_id=rec.id)
        self.assertLessEqual(time() - start, 0.3)
