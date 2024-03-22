# Git Configuration Tool

## Overview

This tool provides a graphical user interface (GUI) for managing your Git configuration, including setting user information and deleting Git credentials. It's designed to simplify the process of configuring Git, especially for those who prefer not to use the command line.

## Features

- **Delete Git Credentials:** Allows the removal of saved Git credentials from your system to help manage security and access.
- **Set Git User Info:** Offers a simple way to set your global Git user name and email, with options for personal, company, or custom configurations.
- **List Git Config:** Displays the current Git configuration for easy review.

## Prerequisites

Before you can use the Git Configuration Tool, ensure you have the following installed:

- Git
- Python 3.x
- Tkinter for Python (usually comes with Python)

## Usage

To use the tool, simply run the script with Python:

```bash
python switch-git.py
```

The GUI will launch, providing you with buttons to perform each of the available actions. Follow the prompts as needed to manage your Git configuration.

## Customizing User Info

When setting user info, you can choose between three types of configurations:

1. Personal: Set a predefined personal user name and email.
2. Company: Use company-specific user name and email settings.
3. Custom: Enter your own name and email.

## License

MIT License
