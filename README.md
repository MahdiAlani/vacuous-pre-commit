# vacuous-pre-commit

A [pre-commit](https://pre-commit.com) hook for
[vacuous](https://github.com/MahdiAlani/vacuous), which finds Python tests that
pass no matter what your code does.

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/MahdiAlani/vacuous-pre-commit
    rev: v0.1.0
    hooks:
      - id: vacuous
```

Then:

```console
pre-commit install
```

## Options

Anything `vacuous check` accepts works through `args`:

```yaml
      - id: vacuous
        args: [--min-confidence, certain]
```

## Adopting this on an existing project

A codebase of any age will have findings already. Record them once so the hook
only complains about new ones:

```console
vacuous baseline
git add .vacuous-baseline.json
```

## Why this is a separate repository

`vacuous` is written in Rust. This repository exists so pre-commit can install
it from a prebuilt wheel on PyPI rather than compiling it, which means
contributors don't need a Rust toolchain.

It contains no code — just a pinned dependency on one version of `vacuous`, so
`rev` above maps to exactly one version of the tool. Same arrangement as
[ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit).

## Releasing a new version

When `vacuous` releases, mirror it:

```console
python update.py 0.1.1
git commit -am "Mirror vacuous 0.1.1"
git tag v0.1.1
git push origin main --tags
```

## License

MIT or Apache-2.0, at your option.
