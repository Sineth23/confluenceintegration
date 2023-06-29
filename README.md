# CodeConverse
CodeConverse is a dynamic tool designed to facilitate seamless communication with your GitHub projects. It allows you to generate documentation from any GitHub project and send it directly to your Confluence space. CodeConverse supports a variety of formats including .md, .html, .pdf, and .csv, ensuring a broad range of documentation can be utilized effectively. This branch currently handles the confluence integration (other integrations to follow)

## Features
- Communicate directly with any GitHub project.
- Generate documentation from a repository.
- Send generated documentation to a Confluence project.
- Supports .md, .html, .pdf, .csv formats.

## Getting Started
To set up and run CodeConverse, follow the steps below:

1. **Prepare your Documentation:** Prepare and save the documents you want to send to your Confluence project in the "Created Documentation" directory. The documents must be in either .md, .html, .pdf, or .csv format.

2. **Setup .env file:** Create a .env file in the root directory of the project and include your Confluence credentials and space key in the following format:
   ```
   CONFLUENCE_USERNAME=your-username
   CONFLUENCE_PASSWORD=your-api-key
   CONFLUENCE_SPACE=your-space-key
   ```
   Replace `your-username`, `your-api-key`, and `your-space-key` with your actual Confluence username, API key, and Confluence space key respectively.

3. **Run the Script:** Finally, run the `main.py` Python file. Follow the prompts to select the document you want to send to Confluence.

That's it! Your selected documentation will be sent to the specified Confluence project. 

Feel free to contact us if you face any issues. Happy documenting with CodeConverse!

## Contribution
Your contributions are always welcome! Please feel free to submit a pull request, create an issue or reach out directly if you have something you'd like to add or modify.

