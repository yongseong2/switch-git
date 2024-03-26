# GitHub User Switch Tool

## Overview

This tool provides a graphical user interface (GUI) for managing your Git and GitHub configurations. It simplifies the process of switching between different Git user profiles and managing GitHub credentials, especially for users who manage multiple accounts or prefer a GUI over command-line tools.

## Features

- **Create Git User**: Allows users to create a new Git user profile by providing a name, email, and GitHub Personal Access Token. This information is saved for future use.
- **Set Git User Info**: Enables setting or switching the global Git user name, email, and credentials based on saved profiles.
- **Delete Git Credentials**: Offers the option to remove saved Git credentials from your system to manage security and access.
- **List Git Config**: Displays the current Git configuration for easy review and verification.

## Prerequisites

Before using the Git Configuration Tool, please ensure you have the following installed:

- Git
- Python 3.x
- Tkinter for Python (usually comes pre-installed with Python)

## Installation

No additional installation steps are required beyond having Python and Git installed on your system. Simply download the `switch-git.py` script to your local machine.

## Usage

To use the tool, run the script with Python from your terminal or command prompt:

```bash
python switch-git.py
```

The GUI will launch, providing you with buttons to perform each of the available actions. Follow the on-screen prompts to manage your Git and GitHub configurations.

## Obtaining a GitHub Personal Access Token

To create or switch user profiles with GitHub credentials, you'll need a Personal Access Token (PAT). Follow these steps to create one:

1. Log in to your GitHub account.
2. Go to Settings > Developer settings > Personal access tokens.
3. Click on the "Generate new token" button.
4. Give your token a descriptive name, select the scopes or permissions you'd like to grant this token, and click "Generate token".
5. Copy the token to your clipboard. **Note**: For security reasons, GitHub will not show the token again, so ensure you save it somewhere safe.

## Customizing User Info

When creating a new Git user profile, you have the option to customize the user name, email, and associate a GitHub Personal Access Token with the profile. This allows for easy switching between different configurations depending on your workflow.

## License

This project is licensed under the MIT License.
