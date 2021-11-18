# Overwrite
## _Make Overwrite More flexible In Python_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A Lite Package focuses on making overwrite and mending functions easier and more flexible. Certain Method performs differently in Certain Condition in an event queue. Certainly used for mending or expanding finished Projects without modifying existed Codes.

- No Origin Codes Changes, Injection with Licenses
- None Invasive Embed Way, More Flexible
- ✨Easy to use✨

## Installation

Overwrite requires [Python](https://www.python.org/) 3.6+ to run.

Simply install with one-line pip command.

```shell
pip install Overwrite
```
## How to Use

**Set a license**
Any type of Cipher-text is satisfactory. Set _int 0_ as example.

```python
_license = 0
```
**Defined function**
Mending function, used for _overwrite_ previous method.

```python
def func():
    return
```
**Register Function to _Event queue_.**

1. _Event_queue_type (string)_: 
   Register with the same _Event_queue_type_ will be added to the same event queue (in registration order).
2. _times (integer)_: 
   The times this function calling is affected. (if affected forever, set times to _-1_)
3. __license (any)_: 
   Used to identify whether the modification is valid and distinguish between different overwrite events.
4. _func (function)_: 
   Mending function, used for overwriting.

```python
Overwrite = Overwrite()
Overwrite.Butler.register('Register_type', times, _license, func)
```

```python
# Add overwrite entrance to function
@Overwrite.entrance(catalog='Register_type')
def affected_func():
    return
```
**Add the License Claim**
If the license is valid, the registered function _affected_func_ will be modified and completely overwritten by _func_. 

```python
# Claim above where the function is Called
Overwrite.claim(_license)
affected_func()
```
The Performance above is same as:
```python
func()
```
## Features

**Complex Overwrite**

```python
Overwrite.Butler.register('Event_queue_type_A', 1, license_A, func_A)
Overwrite.Butler.register('Event_queue_type_A', 2, license_B, func_B)
Overwrite.Butler.register('Event_queue_type_B', 1, license_B, func_C)
```
```python
def func_A():
    print('1')
    return
def func_B():
    print('2')
    return
def func_C():
    print('3')
    return
```
```python
@Overwrite.entrance(catalog='Event_queue_type_A')
def affected_func_A():
    print('A')
    return
@Overwrite.entrance(catalog='Event_queue_type_B')
def affected_func_B():
    print('B')
    return
```
Different _license_ claiming leads to different way of overwriting. After several times calling set before, the performance of modified function will change back to origin again as a result of event queue gets empty.
The program works as below:

```python
@Overwrite.claim(license_B)
affected_func_A() # Output: 2
@Overwrite.claim(license_A)
affected_func_A() # Output: 1
@Overwrite.claim(license_B)
affected_func_A() # Output: 2
@Overwrite.claim(license_A)
affected_func_A() # Output: A
@Overwrite.claim(license_B)
affected_func_A() # Output: A
@Overwrite.claim(license_B)
affected_func_B() # Output: 3
@Overwrite.claim(license_B)
affected_func_B() # Output: B
```
**Get Catalog Name and Available Licenses of Original Function**

```python
Overwrite.Butler.get(affected_func)
-> dict {'catalog_name': str, 'available_license': list[str]}
```

**Browse the Event Queue**

Print details for _Event Queue_:

```python
Overwrite.Queue.print(catalog: str)
```

Get length of _Event Queue_:

```python
Overwrite.Queue.len(catalog: str)
```

Get _Event Queue_ as following type:

```python
Overwrite.Queue.get(catalog: str)
```

```python
[{'times_left': int, 'license': any, 'function_name': str}, 
 {'times_left': int, 'license': any, 'function_name': str},
 {'times_left': int, 'license': any, 'function_name': str},]
```

**Directly manipulate the Event Queue**

Class Queue redefined, making it compatible with _Pythonic_ Style Commands as below:

```python
Overwrite.Queue.append(catalog: str, event: list)
Overwrite.Queue.pop(catalog: str, index: int)
Overwrite.Queue.replace(catalog: str, event: list, index: int)
Overwrite.Queue.clear(catalog: str)
```

## Threading

For multi-threaded function overrides, the event queue is cross-threaded, and the order of event completion depends on the total program time sequence, asynchrony may cause event order confusion.

## Development
**Version:**
*2021.11.18 (0.0.1)*
**Author:** 
_Zack the White_,  _Qcmcmc_
**Email Contact:**
[_**Zack the White**_](ssongaj@connect.ust.hk)
[_**Qcmcmc**_](2778512552@qq.com)

## License

[**MIT**](https://opensource.org/licenses/MIT)
