# Python Filesystem Reference

This reference covers common `pathlib`, built-in file I/O, `os`, and `shutil` operations.
Return types describe the usual successful result; filesystem errors can still raise exceptions.

## 1. `pathlib.Path` properties

| Property       | Return type       | Description                                                                                                                              |
| -------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `path.name`    | `str`             | Returns the final path component, usually the filename including its extension.                                                          |
| `path.stem`    | `str`             | Returns the final filename without its final suffix/extension.                                                                           |
| `path.suffix`  | `str`             | Returns the final filename extension, including the leading dot (for example, `.yaml`). Returns an empty string when there is no suffix. |
| `path.parent`  | `Path`            | Returns the logical parent directory of the path.                                                                                        |
| `path.parts`   | `tuple[str, ...]` | Returns the path split into its individual components.                                                                                   |
| `path.parents` | `Sequence[Path]`  | Returns an immutable sequence of the path's parent paths, from the immediate parent upwards.                                             |

## 2. File modes

The mode is passed to `open(path, mode)`.

| Mode | Return type / result | Description                                                                                           |
| ---- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| `r`  | Text file object     | Opens an existing file for reading text. Fails if the file does not exist.                            |
| `w`  | Text file object     | Opens a file for writing text. Creates it if necessary and truncates an existing file to zero length. |
| `a`  | Text file object     | Opens a file for appending text. Creates it if necessary; new writes go to the end of the file.       |
| `x`  | Text file object     | Creates and opens a new file for writing text. Fails if the file already exists.                      |
| `rb` | Binary file object   | Opens an existing file for reading bytes.                                                             |
| `wb` | Binary file object   | Opens a file for writing bytes. Creates it if necessary and truncates an existing file.               |

For text modes, `open()` returns a text stream. For binary modes, it returns a binary stream. Use the context manager form (`with open(...) as file:`) to close the file reliably.

## 3. `os` functions and attributes

| Function / attribute                | Return type                  | Description                                                                                                                                                                   |
| ----------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `os.getcwd()`                       | `str`                        | Returns the current working directory as an absolute path string.                                                                                                             |
| `os.chdir(path)`                    | `None`                       | Changes the process's current working directory to `path`. The change affects relative paths used by the process afterwards.                                                  |
| `os.listdir(path)`                  | `list[str]`                  | Returns a list of the names of files and directories directly inside `path`. It does not recursively list subdirectories.                                                     |
| `os.mkdir(path)`                    | `None`                       | Creates one directory at `path`. The parent directory must already exist; raises an error if the directory already exists.                                                    |
| `os.makedirs(path, exist_ok=False)` | `None`                       | Creates the directory and any missing parent directories. With `exist_ok=True`, does not fail if the target directory already exists.                                         |
| `os.remove(path)`                   | `None`                       | Deletes the file at `path`. It is intended for files, not non-empty directories.                                                                                              |
| `os.rename(src, dst)`               | `None`                       | Renames or moves a filesystem entry from `src` to `dst`. Whether an existing destination can be replaced depends on the operating system.                                     |
| `os.environ`                        | `os._Environ[str]` (mapping) | Provides a mapping of the process's environment variables. Read values like a dictionary; assigning or deleting entries changes the environment inherited by child processes. |
| `os.getenv("VAR", default=None)`    | `str \| None`                | Returns the value of environment variable `VAR`, or `default` (normally `None`) if it is not set.                                                                             |
| `os.path.exists(path)`              | `bool`                       | Returns `True` if the path exists (or is a valid symlink target); otherwise returns `False`.                                                                                  |
| `os.path.abspath(path)`             | `str`                        | Returns an absolute, normalized path string, based on the current working directory when `path` is relative. It does not require the path to exist.                           |
| `os.path.join(a, b)`                | `str`                        | Joins path components using the platform's path separator. An absolute later component can replace the earlier components.                                                    |

## 4. `pathlib.Path` quick reference

| Operation                                   | Return type      | Description                                                                                                                                                                                    |
| ------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Path.cwd()`                                | `Path`           | Returns the current working directory as a `Path` object.                                                                                                                                      |
| `Path(__file__).resolve()`                  | `Path`           | Resolves the script file path to an absolute path. `__file__` is available in ordinary Python script/module execution, but not necessarily in interactive sessions.                            |
| `Path(__file__).resolve().parent`           | `Path`           | Returns the directory containing the resolved script file.                                                                                                                                     |
| `path.resolve()`                            | `Path`           | Returns an absolute path with `.` and `..` components resolved; by default, also resolves symbolic links where possible.                                                                       |
| `path / "file.txt"`                         | `Path`           | Joins path components and returns a new `Path`. It does not create the file or directory.                                                                                                      |
| `path.name`                                 | `str`            | Returns the final path component, typically the filename including its extension.                                                                                                              |
| `path.stem`                                 | `str`            | Returns the filename without its final suffix.                                                                                                                                                 |
| `path.suffix`                               | `str`            | Returns the final extension, including the dot, or an empty string if there is no extension.                                                                                                   |
| `path.parent`                               | `Path`           | Returns the path's immediate parent directory.                                                                                                                                                 |
| `path.exists()`                             | `bool`           | Returns `True` if the path exists; otherwise returns `False`.                                                                                                                                  |
| `path.is_file()`                            | `bool`           | Returns `True` if the path points to an existing regular file.                                                                                                                                 |
| `path.is_dir()`                             | `bool`           | Returns `True` if the path points to an existing directory.                                                                                                                                    |
| `path.mkdir(parents=False, exist_ok=False)` | `None`           | Creates the directory. Set `parents=True` to create missing parent directories and `exist_ok=True` to avoid an error if the target already exists.                                             |
| `path.read_text(encoding=None)`             | `str`            | Reads the entire text file and returns its contents as a string. Specify an encoding such as `utf-8` for predictable text decoding.                                                            |
| `path.write_text(data, encoding=None)`      | `int`            | Writes the supplied string to the file, replacing existing contents, and returns the number of characters written. Creates the file if needed, but does not create missing parent directories. |
| `path.read_bytes()`                         | `bytes`          | Reads the entire file and returns its contents as bytes, without text decoding.                                                                                                                |
| `path.write_bytes(data)`                    | `int`            | Writes bytes to the file, replacing existing contents, and returns the number of bytes written.                                                                                                |
| `path.unlink(missing_ok=False)`             | `None`           | Deletes the file or symbolic link. With `missing_ok=True`, does not raise an error if the path is missing.                                                                                     |
| `path.iterdir()`                            | `Iterator[Path]` | Returns an iterator yielding a `Path` object for each file and directory directly under this directory. It is not recursive.                                                                   |
| `path.glob("*.py")`                         | `Iterator[Path]` | Returns an iterator yielding paths in this directory that match the pattern. The example matches Python files directly inside the directory.                                                   |
| `path.rglob("*.py")`                        | `Iterator[Path]` | Recursively searches this directory and its subdirectories, yielding paths that match the pattern.                                                                                             |
| `shutil.copy(src, dst)`                     | `str`            | Copies a file's contents and permission mode to `dst`, then returns the destination path as a string.                                                                                          |
| `shutil.move(src, dst)`                     | `str`            | Moves a file or directory to `dst` (or renames it) and returns the resulting destination path as a string.                                                                                     |

## 5. Related `shutil` operations

| Function                    | Return type | Description                                                                                                                                    |
| --------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `shutil.copy(src, dst)`     | `str`       | Copies a file's contents and permission mode. Returns the destination path.                                                                    |
| `shutil.copy2(src, dst)`    | `str`       | Copies a file and attempts to preserve additional metadata, such as modification time. Returns the destination path.                           |
| `shutil.copytree(src, dst)` | `str`       | Recursively copies a directory tree to a new destination and returns the destination path. By default, the destination must not already exist. |
| `shutil.move(src, dst)`     | `str`       | Moves a file or directory and returns the resulting destination path.                                                                          |
| `shutil.rmtree(path)`       | `None`      | Recursively deletes a directory tree and everything inside it. Use with care because the deletion is destructive.                              |

## 6. Important notes

- `Path.iterdir()`, `Path.glob()`, and `Path.rglob()` return iterators, not lists. Convert to a list with `list(path.iterdir())` if you need a list.
- `Path.iterdir()` lists only immediate children; `Path.rglob()` searches recursively.
- `Path.resolve()` and `os.path.abspath()` can produce absolute paths even when the target does not exist, depending on the operation and options used.
- `Path.write_text()` and `Path.write_bytes()` overwrite existing file contents. Use append mode (`open(path, "a")`) when you need to add content.
- `Path.mkdir()` creates directories, while `Path.unlink()` deletes files or symbolic links. Use `Path.rmdir()` for an empty directory and `shutil.rmtree()` for a directory tree.
- Prefer `pathlib` for constructing and inspecting paths. Use `os` for process-level operations such as changing the working directory and accessing environment variables, and `shutil` for copying or moving files and directory trees.
