# Mending
## _Make after-work Mending More flexible In Python_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A Lite Package focuses on making project's after-post mending pythonic and flexible. Certainly used for expanding finished projects without changing exists source code.

- No Origin Codes Changes, Injection with Licenses
- None Invasive Embed Way, More Flexible
- ✨Easy to use✨

## Package Related
Thr Official Packages **ast**, **inspect**, **functools** used.

## Installation

Overwrite requires [Python](https://www.python.org/) 3.6+ to run.

Simply install with one-line pip command.

```shell
pip install Mending
```
## How to Use

**Core Import**

```python
from Mending import Mend
```

**Set a License**
Any type of Cipher-text is satisfactory. Set _int 0_ as example.

```python
_license = 0
```
**Defined Function**
Mending function, used for _overwrite_ previous method.

```python
def func():
    return
```
**Register Function to _Event queue_.**

1. _Register_type (string)_: 
   Register with the same _Event_queue_type_ will be added to the same event queue (in registration order).
2. _times (integer)_: 
   The times this function calling is affected. (if affected forever, set times to _-1_)
3. _license (any)_: 
   Used to identify whether the modification is valid and distinguish between different overwrite events.
4. _func (function)_: 
   Mending function, used for overwriting.

```python
Mend = Mend()
Mend.Butler.register('Register_type', times, _license, func)
```

```python
# Add entrance to function
@Mend.entrance(catalog='Register_type')
def affected_func():
    return
```
**Add the License Claim**
If the license is valid, the registered function _affected_func_ will be modified and completely overwritten by _func_. 

```python
# Claim above the function calling
Mend.claim(_license)
affected_func()
```
The Performance above is same as:
```python
func()
```
## Features

**Complex Overwrite**

```python
Mend.Butler.register('Event_queue_type_A', 1, license_A, func_A)
Mend.Butler.register('Event_queue_type_A', 2, license_B, func_B)
Mend.Butler.register('Event_queue_type_B', 1, license_B, func_C)
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
@Mend.entrance(catalog='Event_queue_type_A')
def affected_func_A():
    print('A')
    return
@Mend.entrance(catalog='Event_queue_type_B')
def affected_func_B():
    print('B')
    return
```
Different _license_ claiming leads to different way of overwriting. After several times calling set before, the performance of modified function will change back to origin again as a result of event queue gets empty.
The program works as below:

```python
@Mend.claim(license_B)
affected_func_A() # Output: 2
@Mend.claim(license_A)
affected_func_A() # Output: 1
@Mend.claim(license_B)
affected_func_A() # Output: 2
@Mend.claim(license_A)
affected_func_A() # Output: A
@Mend.claim(license_B)
affected_func_A() # Output: A
@Mend.claim(license_B)
affected_func_B() # Output: 3
@Mend.claim(license_B)
affected_func_B() # Output: B
```
**Get Catalog Name and Available Licenses of Original Function**

```python
Mend.Butler.get(affected_func)
-> dict {'catalog_name': str, 'available_license': list[str]}
```

**Browse the Event Queue**

Print details for _Event Queue_:

```python
Mend.Queue.print(catalog: str)
```

Get length of _Event Queue_:

```python
Mend.Queue.len(catalog: str)
```

Get _Event Queue_ as following type:

```python
Mend.Queue.get(catalog: str)
```

```python
[{'times_left': int, 'license': any, 'function_name': str}, 
 {'times_left': int, 'license': any, 'function_name': str},
 {'times_left': int, 'license': any, 'function_name': str},]
```

**Directly manipulate the Event Queue**

Class Queue redefined, making it compatible with _Pythonic_ Style Commands as below:

```python
Mend.Queue.append(catalog: str, event: list)
Mend.Queue.pop(catalog: str, index: int)
Mend.Queue.replace(catalog: str, event: list, index: int)
Mend.Queue.clear(catalog: str)
```

## Threading

For multi-threaded function overrides, the event queue is cross-threaded, and the order of event completion depends on the total program time sequence, asynchrony may cause event order confusion. Instantiating Mending for each individual thread is a reasonable solution.

## Development
**Version:**
*2021.11.18 (0.0.8)*

**Author:** 
_Zack the White_,  _Qcmcmc_

**Email Contact:**
[_**Zack the White**_](ssongaj@connect.ust.hk)
[_**Qcmcmc**_](2778512552@qq.com)

## License

[**MIT**](https://opensource.org/licenses/MIT)
