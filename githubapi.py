import requests
import datetime


# my brand function
date = datetime.datetime.now()
assignmentName = "Homework 04a - Develop with the Perspective of the Tester in mind"

def my_brand(assigmentName, date):
    print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")



def  get_GitHubUserRepoCommits(user_id):
    # list to store repo names and number of commits 
    repo_commits = []

    # request to the github api to get repositories based in the user id
    repo_url = f'https://api.github.com/users/{user_id}/repos'
    response = requests.get(repo_url)
    #print(response)

    if response.status_code == 200:
        # Get repositories from the response json
        repositories = response.json()
        #print(repositories)
        # Get repos names
        for repo in repositories:
            repo_name = repo['name']
            
            # request to the github to get number of commits based in the user id and repo name
            commits_url = f'https://api.github.com/repos/{user_id}/{repo_name}/commits'
            commits_response = requests.get(commits_url)

            if commits_response.status_code == 200:
                commits = commits_response.json()
                commit_count = len(commits) # Get number of commits
                repo_commits.append((repo_name, commit_count)) # Add repo name and commit count to the list
            else:
                repo_commits.append((repo_name, 0))  # Add repo name and 0 commit count to the list in case of failure

    else:
        print(f"Failed to retrieve repositories for user {user_id}.") # Print error message in case of failure
    
    return repo_commits # Return the list of repo names and commit counts


# Call the function with a user ID
user_id = 'PALEJADISA'
repo_commits = get_GitHubUserRepoCommits(user_id)
print (repo_commits)
my_brand(assignmentName, date)
for repo, commit_count in repo_commits:
    print(f'Repository: {repo}, Commits: {commit_count}')