# GitHub Private to Public Converter
This Python script automates the process of changing the visibility of your private GitHub repositories to public repositories using the GitHub API. It provides an efficient way to make selected repositories accessible to a broader audience.

## Prerequisites
Before running this script, ensure you have the following prerequisites in place:

1. **GitHub Account**: You need an active GitHub account.

2. **GitHub Personal Access Token**: Generate a GitHub Personal Access Token to authenticate with the GitHub API. Instructions on creating a token can be found [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). (Login to github, goto settings -> developer settings -> personal access token -> tokens(classic) -> click on "generate new token (classic)" -> tick the checkbox of "repo" -> click generate)

3. **Python**: Ensure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

4. **Required Python Libraries**: Install the required Python libraries using the following commands:
   pip install requests
   pip install pygithub

## Usage
1. Clone or download this repository to your local machine.

2. Open the Python script (github_private_to_public.py) in a text editor.

3. Replace the following variables in the script with your own values:
   username: Your GitHub username.
   access_token: Your GitHub Personal Access Token.

4. Save the script with your changes.

5. Open a terminal or command prompt and navigate to the directory containing the script.

6. Run the script using the following command:
   python github_private_to_public.py

The script will make API requests to GitHub to change the visibility of your selected private repositories to public. It will provide feedback on the status of each repository's visibility change.

## License
This script is provided under the MIT License. You are free to use and modify it as needed.

## Acknowledgments
This script utilizes the GitHub API to automate the process of changing repository visibility. Special thanks to the GitHub team for providing this API.
Please use this script responsibly and be aware that making repositories public may affect their accessibility and visibility to a broader audience.

Happy coding!
