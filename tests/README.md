# Tests

As part of any decent app, there are tests that are global to the whole thing.

## Helper

You can also do basic tests with curl, for example, to test the plotter.

```bash
curl -v -X POST localhost:8000 -F rawData=@test.csv -F rawOptions=@test.json
```