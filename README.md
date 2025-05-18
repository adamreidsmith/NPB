# Nested Progress Bar (NPB)

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) A `tqdm`-like progress bar that elegantly supports nested iterations, allowing you to track progress through multiple loops simultaneously without garbled output.

---

## 🌟 Overview

The **NPB** package provides a flexible and easy-to-use progress bar utility for Python applications. Its key feature is the seamless handling of nested loops, where each loop can have its own progress bar displayed cleanly one above the other. This is particularly useful for complex scripts, data processing pipelines, or any task involving iterative operations at multiple levels.

NPB aims to offer a user experience similar to the popular `tqdm` library but with a specific focus on robust nested progress indication.

---

## ✨ Features

* **Nested Loop Support:** Display multiple progress bars concurrently for nested iterations.
* **`tqdm`-like Interface:** Familiar and intuitive API.
* **Customizable Appearance:**
    * Change the fill character of the progress bar.
    * Set custom descriptions for each bar.
    * Adjust the width (number of columns) of the progress bar.
    * Apply text and background colors.
    * Enable a fun rainbow mode for the progress bar text! 🌈
* **Informative Display:**
    * Iteration counter (e.g., `10/100`).
    * Elapsed and estimated remaining time.
    * Current iteration rate (iterations per second or seconds per iteration).
    * Average iteration rate.
* **Dynamic Updates:** Progress bars update at a configurable interval.
* **Disable Option:** Easily disable progress bars for clean logs or non-interactive environments.
* **Error Handling:** Gracefully handles exceptions during iteration, attempting to reset terminal state.
* **`nrange` Shortcut:** A convenient wrapper for `NPB(range(...))`.
<!-- 
---

## 🛠️ Installation

```bash
pip install NPB
``` -->

-----

## 🚀 Usage

### Basic Usage

Wrap any iterable with `NPB` to display a progress bar:

```python
import time
from NPB import NPB

for i in NPB(range(100), desc="Outer Loop"):
    time.sleep(0.05)
```

### Nested Progress Bars

Simply wrap inner loop iterables with `NPB` as well. The bars will be displayed one above the other.

```python
import time
from NPB import NPB, nrange

for i in NPB(range(5), desc="Level 1"):
    for j in NPB(range(20), desc="Level 2", text_color="yellow", bg_color="blue"):
        # For the innermost loop, we can use nrange for convenience
        for k in nrange(20, desc="Level 3", text_color="cyan", rainbow=True, update_interval=0.005):
            time.sleep(0.005)
    time.sleep(0.1)

print("All done!")
```

### `nrange()` Shortcut

For simple range-based loops, `nrange()` is a convenient alternative to `NPB(range(...))`:

```python
from NPB import nrange
import time

for i in nrange(10, desc="My Task"):
    time.sleep(0.1)
```

-----

## ⚙️ API and Customization

The main class is `NPB`. It is initialized as follows:

```python
NPB(
    iterable,
    /,
    *,
    length: Optional[int] = None,
    desc: Optional[str] = None,
    fill_char: str = '█',
    update_interval: float = 0.05,
    disable: bool = False,
    ncols: Optional[int] = None,
    text_color: Optional[str] = None,
    bg_color: Optional[str] = None,
    rainbow: bool = False,
    # Options:
    counter: bool = True,
    timer: bool = True,
    rate: bool = True,
    avg_rate: bool = False
)
```

### Parameters

  * `iterable` (**required**): The iterable to track.
  * `length` (`Optional[int]`): The total number of iterations. NPB tries to get this using `len(iterable)`. Provide if `len()` is unavailable. Default: `None`.
  * `desc` (`Optional[str]`): A short description for the progress bar. Displayed on the left. Default: `None`.
  * `fill_char` (`str`): The character used to fill the progress bar. Default: `'█'`.
  * `update_interval` (`float`): Minimum time interval (in seconds) between progress bar updates. Default: `0.05`.
  * `disable` (`bool`): If `True`, the progress bar is completely disabled, and `NPB(iterable, disable=True)` simply returns the original `iterable`. Default: `False`.
  * `ncols` (`Optional[int]`): The width of the entire progress bar string (in characters). If `None`, it uses the full terminal width. Default: `None`.
  * `text_color` (`Optional[str]`): Color for the progress bar text. Available colors: `'black'`, `'red'`, `'green'`, `'yellow'`, `'blue'`, `'magenta'`, `'cyan'`, `'white'`. Default: `None` (uses terminal default).
  * `bg_color` (`Optional[str]`): Background color for the progress bar text. Same color options as `text_color`. Default: `None`.
  * `rainbow` (`bool`): If `True`, the progress bar text cycles through rainbow colors. Overrides `text_color` if both are set. Default: `False`.
  * `counter` (`bool`): If `True`, display the iteration count (e.g., `X/Y` or `Xit`). Default: `True`.
  * `timer` (`bool`): If `True`, display elapsed and estimated remaining time (e.g., `MM:SS<HH:MM:SS`). Default: `True`.
  * `rate` (`bool`): If `True`, display the current iteration rate. Default: `True`.
  * `avg_rate` (`bool`): If `True`, display the average iteration rate. Default: `False`.
<!-- 
### Example with Customizations

```python
from NPB import NPB
import time

data = list(range(200))

with NPB(
    data,
    desc="Processing Data",
    fill_char="=",
    update_interval=0.1,
    ncols=80,
    text_color="green",
    avg_rate=True
) as pbar:
    for item in pbar:
        time.sleep(0.02)
        if item == 100:
            # You can potentially update description or other properties dynamically
            # (Note: Direct dynamic update of description is not shown in the provided code,
            # but typically progress bars might offer a pbar.set_description() method.
            # For NPB, description is set at initialization of each bar.)
            pass
``` -->

-----

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

-----

Happy iterating\! 🎉
