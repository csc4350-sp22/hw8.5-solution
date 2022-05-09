import unittest
from unittest.mock import MagicMock, patch
from database import Rating, undo_last_review


class TestParenthesesToRemove(unittest.TestCase):
    def setUp(self):
        self.mock_db_for_test = [
            Rating(rating=5, username="jomart", timestamp=20),
            Rating(rating=3, username="tramoj", timestamp=15),
        ]

    def mock_delete(self, obj):
        self.mock_db_for_test.remove(obj)

    def test_undo_last_review(self):
        # demo-ing three kinds of patching here
        # you can make all of these ways equivalent to each other so it's really just a matter of
        # preference.
        with patch("database.Rating.query") as mock_query:  # have to mock query and not
            with patch("database.db.session.delete", self.mock_delete):
                with patch(
                    "database.db.session.commit",
                    lambda: True,  # lambda: True is a function that does nothing
                ):  # meaningless function
                    mock_query.all.return_value = self.mock_db_for_test
                    self.assertEqual(len(self.mock_db_for_test), 2)
                    # we check two things -- that the correct review is returned, and that the "database"
                    # (actually a list defined above) gets an item removed
                    self.assertEqual(self.mock_db_for_test[0], undo_last_review())
                    self.assertEqual(len(self.mock_db_for_test), 1)


if __name__ == "__main__":
    unittest.main()
