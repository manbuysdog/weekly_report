"""
github
"""
import json
import re

import requests

GITHUB_URL = "http://github/api/graphql"
PROD_QUERY = {"query": """query {
                            organization(login:"HPC") {
                                name,
                                projectsUrl,
                                project(number:5) {
                                    name
                                    url
                                    columns (first: 10) {
                                        nodes {
                                            id
                                            name
                                            cards(first: 100) {
                                                nodes {
                                                    id
                                                    databaseId
                                                    content {
                                                        ... on Issue {
                                                            id
                                                            number
                                                            title
                                                            labels (first:10) {
                                                                nodes {
                                                                    name
                                                                    color
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }"""}

TEST_QUERY = {"query": """query {
                            repository(owner:"williamr", name:"weekly_report") {
                                name,
                                projectsUrl,
                                project(number:1) {
                                    name
                                    url
                                    columns (first: 10) {
                                        nodes {
                                            id
                                            name
                                            cards(first: 100) {
                                                nodes {
                                                    id
                                                    databaseId
                                                    content {
                                                        ... on Issue {
                                                            id
                                                            number
                                                            title
                                                            labels (first:10) {
                                                                nodes {
                                                                    name
                                                                    color
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }"""}


def get_github_token():
    """

    :return: github token
    """
    return "xxx"


def get_columns_and_issues(query):
    """

    :param query:
    :return:
    """
    response = requests.post(GITHUB_URL, data=json.dumps(query),
                             headers={"Authorization": "token {}".format(get_github_token())})
    github_data = response.json()

    if 'organization' in github_data['data']:
        repo_key = 'organization'
    else:
        repo_key = 'repository'

    for col in github_data['data'][repo_key]['project']['columns']['nodes']:
        print(col['name'])
        for issue in col['cards']['nodes']:
            # get estimate label if there is one
            estimate_labels = [label['name'] for label in issue['content']['labels']['nodes'] if
                               label['color'] == '444444']
            # if there is no estimate label write TBD
            if not estimate_labels:
                estimate = "TBD"
            else:
                # use the first estimate if there is more than one
                estimate = re.match(r"([\d.]+)d", estimate_labels[0]).group(1)

            print("#{}".format(issue['content']['number']), issue['content']['title'],
                  "({})".format(estimate))
        print('')

    return github_data


def archive_done(done_cards):
    """

    :param done_cards:
    :return:
    """
    for card in done_cards:
        card_id = card["id"]
        issue_id = card["content"]["id"]
        move_done_to_archive(card_id, issue_id)


def move_done_to_archive(card_id, issue_id):
    """
    Moves all the issues in the Done column to the Archive project
    :return: number of issues moved - integer
    """

    # if the issue isn't in the done column of the pipeline project then raise an error
    # raise IssueNotDoneError

    # if the issue isn't closed then raise an error
    # raise IssueNotClosedError

    archive_column_id = "MDEzOlByb2plY3RDb2x1bW4yMDY="
    add_issue_to_project_column(archive_column_id, issue_id)
    delete_card(card_id)
    return


def add_issue_to_project_column(column_id, issue_id):
    """

    :param column_id:
    :param issue_id:
    :return:
    """
    mutation = {"query": """mutation {
                                    addProjectCard(input: {projectColumnId: "%s", contentId: "%s"}) {
                                        projectColumn {
                                            name  
                                        }                                         
                                    }
                            }""" % (column_id, issue_id)}

    response = requests.post(GITHUB_URL, data=json.dumps(mutation),
                             headers={"Authorization": "token {}".format(get_github_token())})

    return response.json()


def delete_card(card_id):
    """

    :param card_id:
    :return:
    """
    mutation = {"query": """mutation {
                                deleteProjectCard(input: {cardId: "%s"}) {
                                    column {
                                        name  
                                    }                                         
                                }
                            }""" % (card_id)}

    response = requests.post(GITHUB_URL, data=json.dumps(mutation),
                             headers={"Authorization": "token {}".format(get_github_token())})

    return response.json()


def get_issue_id_from_number(issue_number):
    """

    :param issue_number:
    :return:
    """
    query = {"query": """query {
                            repository(owner:"williamr", name:"wweekly_report") {
                                issue(number: %d) {
                                    id
                                }
                            }
                        }""" % (issue_number)}

    response = requests.post(GITHUB_URL, data=json.dumps(query),
                             headers={"Authorization": "token {}".format(get_github_token())})

    return response.json()['data']['repository']['issue']['id']


def get_projects():
    """

    :return:
    """
    query = {"query": """query {
                            repository(owner:"williamr", name:"weekly_report") {
                                projects (first: 10){
                                    nodes {
                                        id
                                        name
                                        columns (first: 10) {
                                            nodes {
                                                id
                                                name
                                            }
                                        }
                                    }
                                }
                            }
                        }"""}

    response = requests.post(GITHUB_URL, data=json.dumps(query),
                             headers={"Authorization": "token {}".format(get_github_token())})

    return response.json()

# $ curl -H 'Authorization: token bea16a7c491d26276e155d1cd523b26376c94078'
# -H 'Accept: application/vnd.github.inertia-preview+json' http://github/api/v3/projects/24/columns

# curl -H "Authorization: bearer bea16a7c491d26276e155d1cd523b26376c94078" http://github/api/graphql
