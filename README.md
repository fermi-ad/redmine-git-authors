# Generate authors from Redmine commit history

## Process

### Use the browser to get the Redmine project/repo identifiers

You can copy and paste [./redmineURLGenerator.js](./redmineURLGenerator.js) into your browser console once you are on the repository page for a given project. The console will output a list of repository names.

### Build the projects.json file

The [./projects.json](./projects.json) file is a config file that contains a list of projects and their corresponding Redmine repositories. This information is used to access the git repos directly on the remote Redmine machine.

The general structure of the projects.json file is as follows:

```json
{
    "<project1_name>": [
        "<repo1_name>",
        "<repo2_name>",
        "<repo3_name>",
        "<repo4_name>"
    ],
    "<project2_name>": [
        "<repo1_name>",
        "<repo2_name>",
        "<repo3_name>",
        "<repo4_name>"
    ]
}
```

### Get the authors

Next we run the [./getAuthors.sh](./getAuthors.sh) script to get the authors for each project. The script will output a unique list of authors for each project to the file [./authors.txt](./authors.txt).

### Transform usernames

If you want to transform the usernames to something else, you can do so by editing the [./usernames.json](./usernames.json) config.

The general structure of the usernames.json file is a map of username to transformed name:

```json
{
    "<username1>": "<transformed_username1>",
    "<username2>": "<transformed_username2>",
    "<username3>": "<transformed_username3>",
    "<username4>": "<transformed_username4>"
}
```

If you already ran the [./getAuthors.sh](./getAuthors.sh) script, you need to run it again to update the [./authors.txt](./authors.txt) file with the new usernames.
