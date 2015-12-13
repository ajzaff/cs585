# cs585
Distributional dependency semantics for CS585 Final Project

## Dependencies 

This project depends on this [CoreNLP parser server](https://github.com/dasmith/stanford-corenlp-python) running on `127.0.0.1:8000`.

You will need to tell this package where that is located somehow.
Optionally add a file named `settings.json` with the following detail:

```json
{
	"parserpath": "/path/to/parser/"
}
```

It also uses [Stanford Dependencies](https://github.com/dmcc/PyStanfordDependencies).
Get this with `pip install PyStanfordDependencies`.
