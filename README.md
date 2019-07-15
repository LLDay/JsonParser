# Json Parser #
## Description ##
    
This module provides the `JsonFile` class to read and modify a created json-file or creating a new one.

## Example ##
Json-file before modification:
```json
{
    "old key": "old value",
    "key": "required value" 
}
```

Code:
```python
from json_parser import JsonFile, JsonList, JsonObject

my_json = JsonFile('path')
read_value = my_json['key']

my_json['old key'] = 'changed value'
my_json['digit'] = -1.156
my_json['null'] = None
my_json['true'] = True
my_json['list_name'] = JsonList(1, 2, 3)
my_json['list_name'].append(4)
my_json['obj_name'] = JsonObject({'month': 'Dec'}, day=18)
my_json['obj_name']['year'] = 2010

my_json.close()
```

Json-file after modification:
```json
{
    "old_key": "changed value",
    "key": "required value",
    "digit": -1.156,
    "null": null,
    "true": true,
    "list_name": [
        1, 
        2, 
        3,
        4
    ],
    "obj_name": {
        "month": "Dec",
        "day": 18,
        "year": 2010
    }
}
```