# Json Parser #
## Description ##
    
This module provides classes to read and modify a created json-file or create a new one.

## Features ##
### Dot notation ### 
There is ability to access items using the dot-notation syntax:
```python
my_json = JsonFile('path')
var = my_json.d['path.to.item']
my_json.d['other.path'] = 'value'
my_json.d['key_for_list.1.key']
```
This is equivalent to the following:
```python
my_json = JsonFile('path')
var = my_json['path']['to']['item']
my_json['other']['path'] = 'value'
my_json['key_for_list'][1]['key']
```
To get the value objects must already exist under the `'path'` and `'to'` keys.

Access to keys with spaces is not allowed.

### File safety ###
If you open file only to read and do not want to change the source, don't call `JsonFile.save()` method that rewrites file. This prevents accidental data loss.
If you are sure that you have changed the Json structure correctly, call the `save()` method to apply the changes.

### Refactoring ###
If your json-file has not been formatted, saving will format the file. Optional argument `spaces_number` of the `save()` method changes the indentation width. The default value equals 4 spaces.

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

my_json.save().close()
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