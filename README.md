# JSON Wizard 🧙‍♂️

JSON Wizard is a script that creates an interactive CLI Wizard process to create a JSON file, 
following a configuration.

## How it works?

The main components of this project are:
- A configuration file, which contains a declaration about the wizard process
- The script, that reads this file and starts an interactive wizard
- The result JSON, which will contain the values that the user put inside the wizard

### Configuration JSON

The configuration JSON is the file that contains a description of the fields that the result JSON 
can have.

``` json
[
    {
        "name": "title",
        "type": "string",
        "is_mandatory": true,
        "prompt": "Insert the title of the project:"
    },
    {
        "name": "people",
        "type": "array",
        "prompt": "--- Inserting people ---",
        "items": {
            "type": "object",
            "fields": [
                {
                    "name": "name",
                    "type": "string",
                    "is_mandatory": true
                },
                {
                    "name": "surname",
                    "type": "string",
                    "is_mandatory": true
                },
                {
                    "name": "age",
                    "type": "numeric",
                    "is_mandatory": true
                },
                {
                    "name": "pets",
                    "type": "array",
                    "is_mandatory": true,
                    "items": {
                        "type": "string",
                        "prompt": "Animal name:"
                    }
                }
            ]
        }
    }
]
```
