import datetime
import unittest
from unittest.mock import Mock, patch #unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
from githubapi import get_GitHubUserRepoCommits

# my brand function 
date = datetime.datetime.now()
assignmentName = "Homework 04a - Develop with the Perspective of the Tester in mind"
def my_brand(assigmentName, date):
    print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")


class TestGetGitHubUserRepoCommits(unittest.TestCase):

    @patch('githubapi.requests.get') #The patch() decorator / context manager makes it easy to mock classes or objects in a module under test. 
    def test_get_GitHubUserRepoCommits_sucess(self, mock_requests_get):
        ###Mock the response from the GitHub API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            #Example {'name': 'About-Us-'}, {'name': 'hello-world'}, {'name': 'MySpotListApi'}, {'name': 'Triangle567'}, {'name': 'vanilla'}
        ]
        mock_requests_get.return_value = mock_response

        ###Call the function with a user ID
        user_id = 'PALEJADISA'
        #get_GitHubUserRepoCommits
        repo_commits = get_GitHubUserRepoCommits(user_id)

        ###### Check that the function returns the expected result
        #ORIGINALexpected_result = [('repo1', 0), ('repo2', 0)]
        expected_result = [('repo1', 2), ('repo2', 2)]
        #expected_result = [('About-Us-', 14), ('hello-world', 3),('MySpotListApi', 0), ('Triangle567', 10), ('vanilla', 4)]
        ##########[('About-Us-', 14), ('hello-world', 3), ('MySpotListApi', 0), ('Triangle567', 10), ('vanilla', 4)]
        self.assertEqual(repo_commits, expected_result)

    
    @patch('githubapi.requests.get')
    def test_get_GitHubUserRepoCommits_fail(self, mock_requests_get):
        # Mock a failed response from the GitHub API
        mock_response = Mock()
        mock_response.status_code = 404  # if non found is the status code
        mock_requests_get.return_value = mock_response

        # Call the function with a user ID
        user_id = 'PALEJADISA'
        repo_commits = get_GitHubUserRepoCommits(user_id)

        # Check that the function returns an empty list for failed API response
        self.assertEqual(repo_commits, [])

if __name__ == '__main__':
    my_brand(assignmentName, date)
    unittest.main()