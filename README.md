# git-matrix

Printing short messages on github's activity screen

## Usage

```sh
$ python gitmatrix.py "2017-06-25" "Hello World!"`
```
Accidentally, this particular input-output mapping is the entire reason I wrote this little program.

## Testing

Using the built in `unittest` module, the following command in the project root does the trick:

```
$ python -m unittest tests
```

## TODO

   - More (and less trivial) tests
   - Smart starting pixel (ie.: checking if start date is reasonable)
   - Docstrings for functions
   - proper license?

## License

MIT