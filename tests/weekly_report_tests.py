"""
a docstring
"""
import unittest

class WeeklyReportTestCase(unittest.TestCase):
    def test_simple(self):
        """
        :return:
        """
        self.assertTrue(1 == 1)



# def test_get_columns_and_issues(self):
#     """

#     :return:
#     """
#     query = TEST_QUERY
#     #query = PROD_QUERY
#     retval = get_columns_and_issues(query)
#     self.assertTrue(retval is not None)

# def test_add_card_to_project(self):
#     """

#     :return:
#     """
#     column_id = 1
#     issue_id = 2
#     add_issue_to_project_column(column_id, issue_id)


# def test_get_issue_id(self):
#     """

#     :return:
#     """
#     get_issue_id_from_number(1)


# def test_get_projects(self):
#     """

#     :return:
#     """
#     get_projects()


# def test_move_done_to_archive(self):
#     """

#     :return:
#     """
#     card_id = "MDExOlByb2plY3RDYXJkMjk0Mw=="
#     issue_id = "MDU6SXNzdWUyNzY2"
#     move_done_to_archive(card_id, issue_id)

# def test_archive_done(self):
#     """

#     :return:
#     """
#     project_info = get_columns_and_issues(TEST_QUERY)
#     archive_done(
#         project_info['data']['repository']['project']['columns']['nodes'][2]['cards']['nodes'])
