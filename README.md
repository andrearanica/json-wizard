# JSON Wizard 🧙‍♂️

JSON Wizard is a script that creates an interactive CLI Wizard process to create a JSON file following a given structure.

## How it works?

The main components of this project are:
- A configuration file, which contains a declaration about the wizard process
- The script, that reads this file and starts an interactive wizard


### Configuration JSON

The configuration JSON is the file that contains a description of the fields that the result JSON can have.

The configuration is made by items, and each item can have the following fields:
- `name`: the key of the item
- `type`: it can be `numeric`, `string`, `array`, `object`
- `prompt`: if it is an elementary type (`numeric` and `string`), the message that the wizard will show when asking its value
- `is_mandatory`: if `true`, the wizard will continue asking this parameter until a valid value is given
- `fields`: if the item is an `object`, this field will contain the fields with which the object is composed (see the example below)
- `items`: if the item is an `array`, this field will contain the structure of the items contained in the array (different types of object in the same array is not supported)

This is an example of a configuration JSON.

``` json
{
    "type": "object",
    "fields": [
        {
            "name": "title",
            "type": "string",
            "is_mandatory": true,
            "prompt": "Insert the title of the project:"
        },
        {
            "name": "people",
            "type": "array",
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
}
```
