# Shell Command Plugin - CommandGPT

<img src="https://github.com/graiz/commandGPT/blob/main/.well-known/logo.png" alt="Command GPT" title="Command GPT Logo" width="200" height="200">

The CommandGPT Plugin is a simple Flask-based API that allows users to execute shell commands and receive the results in JSON format. The plugin listens on `localhost:3333` and provides an endpoint `/run` that accepts a shell command as a query parameter and returns the output of the command as a JSON response. This is meant to be used with the OpenAI ChatGPT plug-in system.

The software is currently ALPHA so use it at your own risk.

## ⚠️ Security Warning

This plugin is intended for educational purposes only and should not be used in a production environment without proper security measures in place. Allowing arbitrary shell commands to be executed through an API can be a significant security risk. In a production setting, you should carefully validate and sanitize any input that could be used to execute shell commands, and you should limit the set of allowed commands to a predefined set that is known to be safe.

## Getting Started

### Prerequisites

- Python 3
- Flask
- Flask-CORS

### Installation

1. Clone the repository:  
   `git clone https://github.com/graiz/commandGPT.git`
   
2. Change to the project directory:  
   `cd commandGPT`
   
3. Install the requirements:  
   `pip install -r requirements.txt`
   
### Running the Plugin

1. Start the Flask server:  
   `python main.py`
   
2. Test the API using `curl` or a similar tool:  
   `curl "http://localhost:3333/run?command=ls"`

### Setup in ChatGPT

From ChatGPT, select to add a plug-in via the PlugIn Store. You will need to select that you want to develop your own plug-in. It will now allow you to enter the URL of your local plugin script. If the above test worked, then you should be able to enter `http://localhost:3333` into the custom prompt to let it add your plugin.

## Contributing

Contributions and comments are welcome! Follow my Twitter [@graiz](https://twitter.com/graiz) and [YouTube Channel](https://www.youtube.com/HalfIdeas)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
