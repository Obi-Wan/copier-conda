# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Environment setup

You only need two tools, [conda](https://docs.anaconda.com/free/miniconda/)
and [Copier](https://github.com/copier-org/copier).

```bash
conda create -n templates copier -c conda-forge
```

Then you can clone the repository, enter it and set it up with:

```bash
git clone https://github.com/Obi-Wan/copier-conda
cd copier-conda
make setup
```

## Running tests

To run the tests, use:

```bash
make test
```

## Serving docs

To serve the docs locally, use:

```bash
make docs
```
