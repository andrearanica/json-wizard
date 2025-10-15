# JSON Wizard 🧙‍♂️

JSON Wizard is a script that creates an interactive CLI Wizard process to create a JSON file 
following a given structure.

## How it works?

This script requires a configuration JSON, in which you have to specify the desired fields of the 
result JSON. When the script is started from the shell, it will ask the user to insert the data to 
populate the result JSON and, at the end, the file is written in the given destination. 

### Configuration JSON

The configuration JSON is the file that contains a description of the fields that the result JSON 
will have.

The whole configuration contains nested items; each item is an object that has the following fields:
- `name`: if needed (for example for the fields of an object), the key of the parameter
- `type`: the type of the `Item`. The types can be `string`, `numeric`, `array`, `object`, `map`
- `prompt`: the message to show during the wizard
    - If the item is an `object`, this field will be shown asking for the key of the entry
- `is_mandatory`: if false, the field can have an empty value
- `items`: field that is needed if the item is an `array`; it represents the items that will be 
saved inside the array
- `fields`: field that is needed if the item is an `object`; it is a list of items that will be the 
fields of the object or map
- `pattern`: field that cen be used with `string` items, and lets you choose the regex to match the 
given value; if not passed, the value will be asked again

This is an example of a configuration JSON.

``` json
{
    "type": "object",
    "fields": [
        {
            "name": "schoolName",
            "type": "string",
            "prompt": "Insert the school name",
            "is_mandatory": true
        },
        {
            "name": "classrooms",
            "type": "map",
            "prompt": "Insert the classroom name",
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "fields": [
                        {
                            "name": "studentName",
                            "type": "string",
                            "is_mandatory": true
                        },
                        {
                            "name": "studentSurname",
                            "type": "string",
                            "is_mandatory": true
                        },
                        {
                            "name": "studentAge",
                            "type": "numeric"
                        }
                    ]    
                }
            }
        }
    ]
}
```

After following the wizard, this can be a valid output written by the script.

``` json
{
    "schoolName": "ITIS Paleocapa",
    "classrooms": {
        "5ID": [
            {
                "studentName": "Andrea",
                "studentSurname": "Ranica",
                "studentAge": 20.0
            },
            {
                "studentName": "Mario",
                "studentSurname": "Rossi",
                "studentAge": 0
            }
        ]
    }
}
```

## Usage

To use this script you only have to call it using the bash.
``` bash
python3 json_wizard.py <path-to-configuration-json> <destination-json-path>
```
